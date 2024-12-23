import streamlit as st
import plotly.express as px

# تطبيق CSS لتحسين التنسيق
st.markdown(
    """
    <style>
    .main {
        text-align: center;
    }
    div.stButton > button:first-child {
        margin: auto;
        display: block;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# اختيار اللغة
language = st.sidebar.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])

# العنوان الرئيسي والعنوان الفرعي
if language == "English":
    st.title("BMI and Nutritional Analysis Project")
    st.subheader("Supervised by Ms. Mathayel Al-Otaibi")
else:
    st.title("مشروع: النسبة المئوية في الصحة والتغذية")
    st.subheader("بإشراف أ. مثايل العتيبي")

# إضافة الشريط الجانبي: الهدف، الدور، والنصائح
if language == "English":
    st.sidebar.header("Project Objectives")
    st.sidebar.write("💡 This project aims to highlight the importance of percentages in health and nutrition.")
    st.sidebar.write("💡 It focuses on analyzing body weight and food nutrition to promote healthy habits.")

    st.sidebar.header("Role of Percentages")
    st.sidebar.write("💡 Percentages help you understand nutritional labels.")
    st.sidebar.write("💡 They assist in preventing obesity and maintaining a balanced diet.")

    st.sidebar.header("Nutritional Tips")
    st.sidebar.write("💡 Reduce saturated fats for a healthier heart.")
    st.sidebar.write("💡 Balance your diet with proper protein intake.")
else:
    st.sidebar.header("أهداف المشروع")
    st.sidebar.write("💡 يهدف هذا المشروع إلى إبراز أهمية النسب المئوية في الصحة والتغذية.")
    st.sidebar.write("💡 يركز على تحليل الوزن والغذاء لتعزيز العادات الصحية.")

    st.sidebar.header("دور النسب")
    st.sidebar.write("💡 تساعد النسب في فهم ملصقات التغذية.")
    st.sidebar.write("💡 تسهم في الوقاية من السمنة والحفاظ على نظام غذائي متوازن.")

    st.sidebar.header("نصائح غذائية")
    st.sidebar.write("💡 حاول تقليل الدهون المشبعة لصحة قلب أفضل.")
    st.sidebar.write("💡 حافظ على توازن نظامك الغذائي مع تناول كميات مناسبة من البروتين.")

# تعريف تبويبات التطبيق
tab1, tab2 = st.tabs(["حساب مؤشر كتلة الجسم (BMI)", "تحليل القيم الغذائية"])

# ---- التبويب الأول: حساب BMI ----
with tab1:
    if language == "English":
        st.header("Body Mass Index (BMI) Calculator")
        gender_label = "Select your gender:"
        weight_label = "Enter your weight (kg):"
        height_label = "Enter your height (cm):"
        age_label = "Enter your age (years):"
        activity_label = "Select your activity level:"
        suggested_calories_label = "Suggested daily calories to reach your ideal weight:"
        calorie_distribution_label = "Suggested calorie distribution:"
        warning_msg = "Please enter valid values for weight, height, and age!"
        bmi_result_label = "Your BMI is:"
        ideal_weight_label = "Your ideal weight is:"
        categories = ["Underweight", "Normal weight", "Overweight", "Obesity"]
        activity_levels = {
            "Sedentary (little or no exercise)": 1.2,
            "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
            "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
            "Very active (hard exercise/sports 6-7 days/week)": 1.725,
            "Super active (very hard exercise/physical job)": 1.9,
        }
    else:
        st.header("حساب مؤشر كتلة الجسم (BMI)")
        gender_label = "حدد جنسك:"
        weight_label = "أدخل وزنك (كجم):"
        height_label = "أدخل طولك (سم):"
        age_label = "أدخل عمرك (سنة):"
        activity_label = "حدد مستوى نشاطك البدني:"
        suggested_calories_label = "السعرات اليومية المقترحة للوصول للوزن المثالي:"
        calorie_distribution_label = "تقسيم السعرات الموصى بها:"
        warning_msg = "يرجى إدخال قيم صحيحة للوزن والطول والعمر!"
        bmi_result_label = "مؤشر كتلة الجسم الخاص بك هو:"
        ideal_weight_label = "وزنك المثالي هو:"
        categories = ["نقص في الوزن", "وزن طبيعي", "زيادة في الوزن", "سمنة"]
        activity_levels = {
            "غير نشط (بدون تمارين)": 1.2,
            "نشاط خفيف (تمارين خفيفة 1-3 أيام/الأسبوع)": 1.375,
            "نشاط متوسط (تمارين متوسطة 3-5 أيام/الأسبوع)": 1.55,
            "نشاط عالٍ (تمارين قوية 6-7 أيام/الأسبوع)": 1.725,
            "نشاط شديد (تمارين قوية جدًا/عمل شاق)": 1.9,
        }

    # إدخال البيانات
    gender = st.radio(gender_label, options=["Male", "Female"] if language == "English" else ["ذكر", "أنثى"])
    weight = st.number_input(weight_label, min_value=0.0, step=0.1)
    height_cm = st.number_input(height_label, min_value=0.0, step=1.0)
    age = st.number_input(age_label, min_value=0, step=1)
    activity_level = st.selectbox(activity_label, options=list(activity_levels.keys()))

    # حساب BMI
    if weight > 0 and height_cm > 0 and age > 0:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        st.write(f"{bmi_result_label} {bmi:.2f}")

        if bmi < 18.5:
            st.markdown(f"<span style='color:blue;'>{categories[0]}</span>", unsafe_allow_html=True)
        elif 18.5 <= bmi <= 24.9:
            st.markdown(f"<span style='color:green;'>{categories[1]}</span>", unsafe_allow_html=True)
        elif 25 <= bmi <= 29.9:
            st.markdown(f"<span style='color:orange;'>{categories[2]}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:red;'>{categories[3]}</span>", unsafe_allow_html=True)

        # حساب الوزن المثالي
        if gender == "Male" or gender == "ذكر":
            ideal_weight = 50 + 0.9 * (height_cm - 152)
        else:
            ideal_weight = 45.5 + 0.9 * (height_cm - 152)
        st.write(f"{ideal_weight_label} {ideal_weight:.2f} kg")

        # حساب السعرات المقترحة للوصول للوزن المثالي
        if gender == "Male" or gender == "ذكر":
            suggested_bmr = 10 * ideal_weight + 6.25 * height_cm - 5 * age + 5
        else:
            suggested_bmr = 10 * ideal_weight + 6.25 * height_cm - 5 * age - 161
        suggested_calories = suggested_bmr * activity_levels[activity_level]
        st.write(f"{suggested_calories_label} {suggested_calories:.2f} kcal/day")

        # تقسيم السعرات المقترحة
        carbs = 0.5 * suggested_calories / 4
        protein = 0.2 * suggested_calories / 4
        fats = 0.3 * suggested_calories / 9
        st.subheader(calorie_distribution_label)
        st.write(
            f"Carbohydrates: {carbs:.2f} g/day" if language == "English" else f"الكربوهيدرات: {carbs:.2f} جرام/اليوم")
        st.write(f"Protein: {protein:.2f} g/day" if language == "English" else f"البروتين: {protein:.2f} جرام/اليوم")
        st.write(f"Fats: {fats:.2f} g/day" if language == "English" else f"الدهون: {fats:.2f} جرام/اليوم")
    else:
        st.warning(warning_msg)

# ---- التبويب الثاني: تحليل القيم الغذائية ----
with tab2:
    if language == "English":
        st.header("Nutritional Analysis")
        total_calories_label = "Enter total calories:"
        fat_calories_label = "Enter calories from fat:"
        protein_calories_label = "Enter calories from protein:"
        carbs_calories_label = "Enter calories from carbohydrates:"
        chart_title = "Nutritional Components Percentages"
        results_header = "Analysis Results"
    else:
        st.header("تحليل القيم الغذائية")
        total_calories_label = "أدخل إجمالي السعرات الحرارية:"
        fat_calories_label = "أدخل السعرات الحرارية من الدهون:"
        protein_calories_label = "أدخل السعرات الحرارية من البروتين:"
        carbs_calories_label = "أدخل السعرات الحرارية من الكربوهيدرات:"
        chart_title = "نسب المكونات الغذائية"
        results_header = "نتائج التحليل"

    # إدخال القيم الغذائية
    total_calories = st.number_input(total_calories_label, min_value=0.0, step=1.0)
    fat_calories = st.number_input(fat_calories_label, min_value=0.0, step=1.0)
    protein_calories = st.number_input(protein_calories_label, min_value=0.0, step=1.0)
    carbs_calories = st.number_input(carbs_calories_label, min_value=0.0, step=1.0)

    # حساب النسب المئوية وعرض النتائج قبل الرسم البياني
    if total_calories > 0:
        fat_percentage = (fat_calories / total_calories) * 100
        protein_percentage = (protein_calories / total_calories) * 100
        carbs_percentage = (carbs_calories / total_calories) * 100

        # عرض النتائج نصيًا
        st.subheader(results_header)
        if language == "English":
            st.write(f"Fat percentage: {fat_percentage:.2f}%")
            st.write(f"Protein percentage: {protein_percentage:.2f}%")
            st.write(f"Carbohydrates percentage: {carbs_percentage:.2f}%")
        else:
            st.write(f"نسبة الدهون: {fat_percentage:.2f}%")
            st.write(f"نسبة البروتين: {protein_percentage:.2f}%")
            st.write(f"نسبة الكربوهيدرات: {carbs_percentage:.2f}%")

        # عرض الرسم البياني
        labels = ['الدهون', 'البروتين', 'الكربوهيدرات'] if language == "العربية" else ['Fat', 'Protein',
                                                                                       'Carbohydrates']
        values = [fat_calories, protein_calories, carbs_calories]
        fig = px.pie(values=values, names=labels, title=chart_title)
        st.plotly_chart(fig)