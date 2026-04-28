import gradio as gr
from bot_logic import BBB_Smart_Session
import os

bot = BBB_Smart_Session()

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 BB RENDER BOT")
    num = gr.Textbox(label="Number")
    btn = gr.Button("Get OTP")
    out = gr.Label(value="Ready")
    btn.click(bot.request_otp, inputs=[num], outputs=[out])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    demo.launch(server_name="0.0.0.0", server_port=port)
