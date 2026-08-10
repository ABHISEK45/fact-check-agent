from database import SessionLocal
from models import Report, Claim


def save_report(filename, claims, results):

    db = SessionLocal()

    try:
        # Create report
        report = Report(
            filename=filename
        )

        db.add(report)
        db.flush()

        # Save claims and verification results
        for claim_data, result in zip(claims, results):

            claim_record = Claim(
                report_id=report.id,

                claim=claim_data["claim"],

                claim_type=claim_data.get(
                    "type",
                    ""
                ),

                search_query=claim_data.get(
                    "search_query",
                    ""
                ),

                verdict=result.get(
                    "verdict",
                    ""
                ),

                confidence=result.get(
                    "confidence",
                    ""
                ),

                correct_fact=result.get(
                    "correct_fact",
                    ""
                ),

                explanation=result.get(
                    "explanation",
                    ""
                )
            )

            db.add(claim_record)

        db.commit()

        return report.id

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()