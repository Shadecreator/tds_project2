# image_encoder.py

import base64
import io

def encode_plot_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_bytes = buf.read()
    base64_img = base64.b64encode(img_bytes).decode('utf-8')
    return f"data:image/png;base64,{base64_img}"
