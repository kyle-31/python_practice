from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# 1. 載入資料
iris = load_iris()

X = iris.data      # 花的特徵，例如花瓣長度、寬度
y = iris.target    # 花的種類答案


# 2. 分成訓練資料與測試資料
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. 建立模型
model = KNeighborsClassifier(n_neighbors=3)


# 4. 訓練模型
model.fit(X_train, y_train)


# 5. 用測試資料預測
y_pred = model.predict(X_test)


# 6. 評估準確率
accuracy = accuracy_score(y_test, y_pred)
print("模型準確率：", accuracy)


# 7. 實際預測一朵新的花
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)

print("預測結果：", iris.target_names[prediction[0]])