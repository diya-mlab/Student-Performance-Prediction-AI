

import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample student dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Previous_Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    "Exam_Marks": [38, 42, 48, 52, 58, 63, 68, 75, 78, 85]
}

df = pd.DataFrame(data)

# Prepare and train the AI model
X = df[["Study_Hours", "Previous_Marks"]]
y = df["Exam_Marks"]

model = LinearRegression()
model.fit(X, y)


# Prediction function
def predict_marks(hours, previous_marks):

    student = pd.DataFrame({
        "Study_Hours": [hours],
        "Previous_Marks": [previous_marks]
    })

    prediction = float(model.predict(student)[0])
    prediction = max(0, min(100, prediction))

    if prediction >= 60:
        category = "Good"
        suggestion = "Good progress! Keep practising regularly."
    elif prediction >= 40:
        category = "Average"
        suggestion = "You can improve with more focused study."
    else:
        category = "Needs Improvement"
        suggestion = "Follow a regular study schedule."

    result_text = (
        f"Predicted Marks: {prediction:.2f}/100\n"
        f"Performance: {category}\n"
        f"Suggestion: {suggestion}"
    )

    return result_text


# Create professional web interface
with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown(
        """
        # 🎓 Student Performance Prediction AI
        ### Intelligent Academic Performance Analysis

        Enter student details to predict examination performance.
        """
    )

    with gr.Row():

        with gr.Column():
            hours = gr.Slider(
                minimum=0,
                maximum=12,
                value=5,
                step=0.5,
                label="Daily Study Hours"
            )

            previous_marks = gr.Slider(
                minimum=0,
                maximum=100,
                value=60,
                step=1,
                label="Previous Examination Marks"
            )

            predict_button = gr.Button(
                "Predict Student Performance",
                variant="primary"
            )

        with gr.Column():
            result = gr.Textbox(
                label="AI Prediction Result",
                lines=5
            )

    predict_button.click(
        fn=predict_marks,
        inputs=[hours, previous_marks],
        outputs=result
    )

    gr.Markdown(
        """
        ---
        **Developed using:** Python | Pandas | Scikit-learn | Gradio

        **Project:** Student Performance Prediction AI
        """
    )


app.launch()
