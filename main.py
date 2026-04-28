import gradio as gr
from bot_logic import BBB_Smart_Session
import os

# Bot ka object banaya
bot_instance = BBB_Smart_Session()

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 BB RENDER BOT")
    num = gr.Textbox(label="Mobile Number (10 Digits)")
    btn = gr.Button("Get OTP")
    out = gr.Label(value="Ready")
    
    # Yahan 'request_otp' hi likhna hai tabhi chalega
    btn.click(bot_instance.request_otp, inputs=[num], outputs=[out])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    demo.launch(server_name="0.0.0.0", server_port=port)
