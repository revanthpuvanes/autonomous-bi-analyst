from utils.data_loader import load_data
from agents.planner import create_plan
from agents.analyst import analyze_data
from agents.reporter import generate_report
from agents.verifier import verify

def run_pipeline():
    question = "Why did sales drop?"

    df = load_data("data/sample.csv")

    print("\n📌 QUESTION:", question)

    # 1. Planner
    plan = create_plan(question)
    print("\n🧠 PLAN:\n", plan)

    # 2. Analyst
    analysis = analyze_data(df, question)
    print("\n📊 ANALYSIS:\n", analysis)

    # 3. Reporter
    report = generate_report(question, analysis)
    print("\n📝 REPORT:\n", report)

    # 4. Verifier (NEW 🔥)
    verification = verify(question, analysis, report)
    print("\n🛡️ VERIFICATION:\n", verification)


if __name__ == "__main__":
    run_pipeline()