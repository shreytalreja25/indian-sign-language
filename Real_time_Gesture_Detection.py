import cv2

# Load the trained sequence model
# sequence_model = load_model('your_sequence_model.h5')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = preprocess_frame(frame)
    processed_frame = np.expand_dims(processed_frame, axis=0)
    features = model.predict(processed_frame)
    features = np.expand_dims(features, axis=0)

    prediction = sequence_model.predict(features)

    if prediction > 0.5:
        cv2.putText(frame, 'welcome home', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Gesture Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
