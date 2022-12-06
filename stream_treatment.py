import pickle
import streamlit as st

# load save model
treatment_model = pickle.load(open('treatment_patient.sav', 'rb'))

# Judul Untuk Web
st.title('Klasifikasi Perawatan Pasien')
st.text('Nama : Bambang Yudho D.A')
st.text('Nim : 191351122')
st.text('Matkul : Business Intelligence')

# Form Input
HAEMATOCRIT = st.text_input('Masukan Hasil Tes hematokrit')

HAEMOGLOBINS = st.text_input('Masukan Hasil Tes Haemagoblins')

ERYTHROCYTE = st.text_input('Masukan Hasil Tes Erythrocyte ')

LEUCOCYTE = st.text_input('Masukan Hasil Tes LEUCOCYTE ')

THROMBOCYTE = st.text_input('Masukan Hasil Tes THROMBOCYTE ')

MCH = st.text_input('Masukan Hasil Tes MCH ')

MCHC = st.text_input('Masukan Hasil Tes MCHC ')

MCV = st.text_input('Masukan Hasil Tes MCV ')

AGE = st.text_input('Masukan  Umur ')

SEX = st.text_input('Masukan Gender Pasien ')



# kode Prediksi
treatment_diagnosis =''

#Button Prediksi
if st.button('Prediksi Tingkat Stress'):
    treatment_prediction = treatment_model.predict([[HAEMATOCRIT,HAEMOGLOBINS,ERYTHROCYTE,LEUCOCYTE,THROMBOCYTE,MCH,MCHC,MCV,AGE,SEX]])

    if(treatment_prediction[0]==0):
        treatment_diagnosis = 'pasien rawat jalan'
    else:
        treatment_diagnosis = 'dalam perawatan pasien'
st.success(treatment_diagnosis)