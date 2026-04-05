from pypdf import PdfReader

from .scripts.supervisior.supervisior import supervisor_check
from .scripts.regenerate.regenerate import regenerate
from .logs.db import save_log
from openai import OpenAI
from .prompts.mixed import company_prompt, email_prompt, supervisior_prompt, regenerate_prompt, brochure_prompt

from dotenv import load_dotenv
import os

load_dotenv()

GITHUB_KEY = os.getenv("GITHUB_KEY")
MODEL_GEN = "gpt-4o-mini"
MODEL_SUPERVISOR = "gpt-4o-mini"
MAX_RETRIES = 2

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_KEY 
)

def generate_content(company):
    """Generate email and brochure for a company."""
    try:
        print(f"🔍 Researching {company}...")
        prompt = company_prompt.format(company_name=company)

        res = client.chat.completions.create(
            model=MODEL_GEN,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )

        insights = res.choices[0].message.content
        print(f"  ✓ {company} research complete")

        # Read base brochure template using absolute path
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            pdf_path = os.path.join(script_dir, "Sponsorship Proposal - Tech Fest.pdf")
            pdf_reader = PdfReader(pdf_path)
            brochure_template_text = ""
            for page in pdf_reader.pages[:2]:  # Read first 2 pages
                brochure_template_text += page.extract_text() + "\n"
        except FileNotFoundError:
            print(f"  ⚠ Warning: PDF not found at {pdf_path}")
            brochure_template_text = ""
        except Exception as e:
            print(f"  ⚠ Warning: Could not read brochure template: {e}")
            brochure_template_text = ""

        # Generate email based on company insights and template
        print(f"  Generating email...")
        prompt = email_prompt.format(company_name=company, insights=insights)
        res_email = client.chat.completions.create(
            model=MODEL_GEN,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}]
        )
        email = res_email.choices[0].message.content.strip()
        print(f"  ✓ Email generated for {company}")

        # Generate brochure based on company insights and template
        print(f"  Generating brochure...")
        prompt = brochure_prompt.format(company_name=company, insights=insights, brochure=brochure_template_text)
        res_brochure = client.chat.completions.create(
            model=MODEL_GEN,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}]
        )
        brochure = res_brochure.choices[0].message.content.strip()
        print(f"  ✓ Brochure generated for {company}")

        return email, brochure
    except Exception as e:
        print(f"✗ Error generating content for {company}: {e}")
        return None, None

def process_company(company):
    """Process a single company: generate, review, and refine content."""
    retries = 0

    email, brochure = generate_content(company)
    
    if email is None or brochure is None:
        print(f"✗ Failed to generate content for {company}")
        return None, None, {"status": "failed", "feedback": "Content generation failed"}

    print(f"📋 Checking with supervisor for {company}...")
    while True:
        result = supervisor_check(company, email, brochure, retries)

        print(f"  Supervisor result: {result['status']} (Score: {result.get('score', 'N/A')})")

        if result["status"] == "approved":
            print(f"  ✓ {company} approved by supervisor")
            save_log(company, email, brochure, result, retries)
            return email, brochure, result

        elif result["status"] == "retry":
            retries += 1
            if retries > MAX_RETRIES:
                result["status"] = "max_retries_exceeded"
                print(f"  ✗ Max retries exceeded for {company}")
                save_log(company, email, brochure, result, retries)
                return email, brochure, result
            
            print(f"  🔄 Regenerating content (attempt {retries})...")
            email, brochure = regenerate(company, email, brochure, result["feedback"], client)

        else:
            print(f"  ✗ Supervisor rejected {company}")
            save_log(company, email, brochure, result, retries)
            return None, None, result
        

companies = ["Google", "Microsoft"]

if __name__ == "__main__":
    try:
        for company in companies:
            result = process_company(company)
            import gc
            gc.collect()  # Force garbage collection to free memory
            if result[2].get("status") == "approved":
                print(f"✓ {company}: Approved")
            elif result[2].get("status") == "max_retries_exceeded":
                print(f"✗ {company}: Max retries exceeded (Score: {result[2].get('score', 'N/A')})")
            else:
                print(f"✗ {company}: {result[2].get('status')}")
    except Exception as e:
        print(f"Error processing companies: {e}")
    finally:
        # Properly close database connections
        from .logs.db import get_connection
        conn_obj, cur = get_connection()
        if cur is not None:
            cur.close()
        if conn_obj is not None:
            conn_obj.close()
        print("DB closed.")