
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

--------------------------------

1. STUDENT PERFORMANCE PREDICTION

--------------------------------

def predict_marks(hours, previous_marks):

student = pd.DataFrame({  
    'Study_Hours': [hours],  
    'Previous_Marks': [previous_marks]  
})  

prediction = model.predict(student)[0]  

prediction = max(0, min(100, prediction))  

# Performance category  

if prediction >= 80:  
    category = "Excellent"  
    suggestion = "Keep up your excellent study routine!"  

elif prediction >= 60:  
    category = "Good"  
    suggestion = "Practice regularly to improve further."  

elif prediction >= 40:  
    category = "Average"  
    suggestion = "Focus more on revision and practice."  

else:  
    category = "Needs Improvement"  
    suggestion = "Strengthen your basics and study consistently."  

# --------------------------------  
# 2. PERFORMANCE CHART  
# --------------------------------  

fig, ax = plt.subplots(figsize=(6, 3))  

labels = ["Previous Marks", "Predicted Marks"]  
values = [previous_marks, prediction]  

ax.bar(labels, values)  

ax.set_ylim(0, 100)  
ax.set_ylabel("Marks")  
ax.set_title("Student Performance Analysis")  

for i, value in enumerate(values):  
    ax.text(i, value + 2, f"{value:.1f}", ha="center")  

plt.tight_layout()  

# --------------------------------  
# 3. PREDICTION RESULT  
# --------------------------------  

result = (  
    f"Predicted Marks: {prediction:.2f}/100\n\n"  
    f"Performance: {category}\n\n"  
    f"Suggestion: {suggestion}"  
)  

return result, fig

--------------------------------

4. PROFESSIONAL WEB INTERFACE

--------------------------------

with gr.Blocks(theme=gr.themes.Soft()) as app:

gr.Markdown(  
    """  
    # 🎓 Student Performance Prediction AI  

    ### Intelligent Academic Performance Analysis  

    Enter student details to predict examination performance.  
    """  
)  

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

    result = gr.Textbox(  
        label="AI Prediction Result",  
        lines=5  
    )  

    chart = gr.Plot(  
        label="Performance Analysis Chart"  
    )  

predict_button.click(  
    fn=predict_marks,  
    inputs=[hours, previous_marks],  
    outputs=[result, chart]  
)  

gr.Markdown(  
    """  
    ---  

    **Developed using:** Python | Pandas | Scikit-learn | Gradio  

    **Project:** Student Performance Prediction AI  
    """  
)

--------------------------------

5. LAUNCH WEB APPLICATION

--------------------------------

app.launch(share=True)
