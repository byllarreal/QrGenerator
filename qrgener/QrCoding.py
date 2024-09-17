import qrcode
import json
from io import BytesIO
from django.core.files import File
from django.forms.models import model_to_dict

class QrCoding:
    def qrcod(self, data):
        qr=qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr_data_dict=model_to_dict(data, fields=['url', 'descripcion', 'vcard', 'email', 'telefono', 'wifi', 'geo'])
        data_content=json.dumps(qr_data_dict)

        qr.add_data(data_content)
        qr.make(fit=True)

        img=qr.make_image(fill='black', back_color='white')
        img_io=BytesIO()
        img.save(img_io, format='PNG')
        img_io.seek(0)
        if data.id is None:
            data.save()

        img_file=File(img_io, name=f'qr_{data.id}.png')

        return img_file

