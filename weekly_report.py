# weekly_report.py

def generate_report(schedule_df):
    """
    Generates a weekly report from the schedule DataFrame.
    """
    try:
        report = "📈 Weekly Progress Report\n\n"
        for index, row in schedule_df.iterrows():
            report += f"• {row['Subject']}: {round(row['Predicted Study Hours'], 2)} hrs planned\n"
        return report
    except Exception as e:
        return f"Error generating report: {e}"
