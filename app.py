import streamlit as st
import pandas as pd

from pdf_utils import extract_text_from_pdf

from verifier import (
    extract_claims,
    search_web,
    verify_all_claims
)

st.set_page_config(
    page_title="Fact Check Agent",
    layout="wide"
)

st.title("📄 Fact Check Agent")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(
        uploaded_file
    )

    st.success(
        "PDF Processed Successfully"
    )

    with st.expander(
        "View Extracted Text"
    ):

        st.text_area(
            "PDF Content",
            text,
            height=300
        )

    if st.button(
        "Extract Claims & Verify Facts"
    ):

        with st.spinner(
            "Extracting claims..."
        ):

            claims = extract_claims(text)

        # Avoid burning credits on huge PDFs
        claims = claims[:15]

        st.subheader(
            "Extracted Claims"
        )

        st.json(claims)

        claims_with_evidence = []

        with st.spinner(
            "Searching live web..."
        ):

            for item in claims:

                claim = item["claim"]

                search_query = item.get(
                    "search_query",
                    claim
                )

                evidence = search_web(search_query)

                st.write("DEBUG EVIDENCE:", evidence)

                claims_with_evidence.append({
                   ...
                 })

                claims_with_evidence.append(
                    {
                        "claim": claim,
                        "search_query": search_query,
                        "evidence": evidence
                    }
                )

        with st.expander(
            "View Search Evidence"
        ):
            st.json(
                claims_with_evidence
            )

        with st.spinner(
            "Verifying claims..."
        ):

            results = verify_all_claims(
                claims_with_evidence
            )

        st.subheader(
            "Fact Check Results"
        )

        rows = []

        for result in results:

            rows.append(
                {
                    "Claim": result.get(
                        "claim"
                    ),
                    "Verdict": result.get(
                        "verdict"
                    ),
                    "Confidence": result.get(
                        "confidence"
                    )
                }
            )

        df = pd.DataFrame(rows)

        st.dataframe(
            df,
            width="stretch"
        )

        for result in results:

            st.markdown("---")

            st.write(
                f"### {result.get('claim')}"
            )

            st.write(
                f"**Verdict:** {result.get('verdict')}"
            )

            st.write(
                f"**Confidence:** {result.get('confidence')}"
            )

            st.write(
                f"**Correct Fact:** {result.get('correct_fact')}"
            )

            st.write(
                f"**Explanation:** {result.get('explanation')}"
            )

            sources = result.get(
                "sources_used",
                []
            )

            if sources:

                st.write(
                    "**Sources Used:**"
                )

                for source in sources:
                    st.write(source)

        csv = df.to_csv(
            index=False
        )

        st.download_button(
            label="📥 Download Report",
            data=csv,
            file_name="fact_check_report.csv",
            mime="text/csv"
        )