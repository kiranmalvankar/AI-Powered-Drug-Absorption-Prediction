import streamlit as st

from rdkit import Chem


from prediction_utils import (
    predict_permeability_with_ad
)

st.title("Permeability Prediction Tool")

st.write(
    "Predict permeability (logPapp) from molecular SMILES."
)

smiles = st.text_input(
    "Enter SMILES"
)

if st.button("Predict"):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:

        st.error("Invalid SMILES")

    else:

        img = Draw.MolToImage(
            mol,
            size=(400, 300)
        )

        st.image(
            img,
            caption="Molecular Structure"
        )

        result = predict_permeability_with_ad(
            smiles
        )

        st.subheader(
            "Prediction Results"
        )

        st.metric(
            "🧪 Predicted logPapp",
            round(
                result["Predicted logPapp"],
                3
            )
        )

        st.metric(
            "📏 Distance",
            round(
                result["Distance"],
                3
            )
        )

        if result["AD Status"] == "Inside AD":

            st.success(
                f"✅ Applicability Domain: {result['AD Status']}"
            )

        else:

            st.warning(
                f"⚠️ Applicability Domain: {result['AD Status']}"
            )

        if result["Confidence"] == "High":

            st.info(
                f"🔵 Confidence: {result['Confidence']}"
            )

        else:

            st.error(
                f"🔴 Confidence: {result['Confidence']}"
            )
st.markdown("---")

st.subheader("Model Information")

st.write("Algorithm: Random Forest")

st.write(
    "Features: Morgan Fingerprints (2048 bits) + RDKit Descriptors"
)

st.write(
    "Descriptors: MolWt, LogP, TPSA, HBD, HBA, RotB"
)

st.subheader("Dataset Information")

st.write(
    "Training Molecules: 12,290"
)

st.write(
    "Endpoint: Caco-2 Permeability (logPapp)"
)

st.write(
    "Applicability Domain: k-Nearest Neighbors (k=2)"
)

st.write(
    "AD Threshold: 22.853"
)
st.markdown("---")
st.caption(
    "Developed by Kiran Malvankar | Cheminformatics & Machine Learning"
)
st.subheader(
    "Model Validation Metrics"
)

st.write(
    "5-Fold Cross-Validation R²: 0.598 ± 0.009"
)
st.info(
    "Predictions should be interpreted within the Applicability Domain."
)