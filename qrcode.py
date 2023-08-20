import cv2

filename = "C:\\Users\\sgupt\\Desktop\\aham health\\assignment 2\\qrcodedadar.png"

image = cv2.imread(filename)

detector = cv2.QRCodeDetector()

data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

if vertices_array is not None:
  print("QRCode data:")
  print(data)
else:
  print("There was some error")