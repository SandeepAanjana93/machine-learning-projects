import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("emails.csv")

label_map = {"spam": 0, "ham": 1}
df["label"] = df["label"].map(label_map)

X = df["message"]
y = df["label"]

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.3,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Spam", "Ham"]
).plot()

plt.title("Spam Detection - Confusion Matrix")
plt.show()

test_message = ["Congratulations you won free cash"]
test_vector = vectorizer.transform(test_message)
prediction = model.predict(test_vector)

if prediction[0] == 0:
    print("Prediction: SPAM")
else:
    print("Prediction: HAM")