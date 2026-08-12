# Recommendation based on medical condition (9 Classes)

normal = '''**For Normal Eye**
- **Recommendation**:
    - **Routine Eye Care**: Your eye image appears normal with no visible abnormalities. Continue regular eye checkups to maintain eye health.
    - **Eye Health Maintenance**:
      - **Balanced Diet**: Eat foods rich in Vitamin A, C, E, omega-3 fatty acids, lutein, and zinc (leafy greens, carrots, fish, fruits).
      - **Hydration & Sleep**: Proper hydration and sleep support overall eye function.
      - **Limit Screen Strain**: Follow the 20-20-20 rule to reduce digital eye strain.
    - **Next Steps**:
      - Schedule routine eye exams every 1–2 years (or as advised).
      - Seek evaluation if you notice sudden blurriness, floaters, or vision changes.
'''

severe = '''**For Severe Eye Condition**
- **Recommendation**:
    - **Immediate Referral**: Severe stage indicates advanced disease progression and requires urgent evaluation by an ophthalmologist or retinal specialist.
    - **Possible Treatments (Doctor-Dependent)**:
      - **Medication / Injections**: Depending on disease type, anti-VEGF injections or steroids may be required.
      - **Laser Treatment**: In severe retinal cases, laser procedures may be recommended.
      - **Surgery**: Advanced conditions might require surgical intervention.
    - **Lifestyle & Monitoring**:
      - **Strict Follow-ups**: Frequent monitoring is essential to prevent permanent vision loss.
      - **Manage Risk Factors**: Diabetes, hypertension, and smoking can worsen severe eye disease.
    - **Next Steps**:
      - Consult a specialist immediately.
      - Do not delay treatment if you have vision loss, flashes, pain, or black spots.
'''

cataract = '''**For Cataract**
- **Recommendation**:
    - **Ophthalmology Consultation**: Cataract causes clouding of the eye lens and leads to blurry vision and glare sensitivity.
    - **Treatment Options**:
      - **Early Stage**: Stronger glasses, better lighting, anti-glare sunglasses.
      - **Advanced Stage**: **Cataract surgery** is the definitive and most effective treatment.
    - **Lifestyle & Monitoring**:
      - **Reduce UV Exposure**: Wear sunglasses with UV protection.
      - **Avoid Smoking**: Smoking increases cataract progression.
      - **Control Diabetes**: High sugar levels can worsen cataracts.
    - **Next Steps**:
      - Schedule an eye specialist appointment.
      - Consider surgery if vision affects daily life (driving, reading, work).
'''

proliferate_dr = '''**For Proliferative Diabetic Retinopathy (Proliferate_DR)**
- **Recommendation**:
    - **Emergency Specialist Visit**: This is an advanced stage of diabetic retinopathy where abnormal blood vessels grow and may bleed into the eye.
    - **Treatment Options**:
      - **Anti-VEGF Injections**: Helps reduce abnormal vessel growth and swelling.
      - **Laser Photocoagulation (PRP Laser)**: Prevents further bleeding and retinal damage.
      - **Vitrectomy Surgery**: Required if there is significant bleeding or retinal detachment.
    - **Diabetes Control**:
      - **Maintain HbA1c below 7%** (doctor-guided).
      - Control blood pressure and cholesterol.
    - **Next Steps**:
      - Immediate retina specialist consultation.
      - Regular monitoring every 1–3 months depending on severity.
'''

glaucoma = '''**For Glaucoma**
- **Recommendation**:
    - **Urgent Eye Specialist Check**: Glaucoma can damage the optic nerve and lead to irreversible vision loss if untreated.
    - **Treatment Options**:
      - **Eye Drops**: To reduce intraocular pressure (IOP).
      - **Laser Therapy**: Helps improve fluid drainage.
      - **Surgery**: In advanced cases to control pressure.
    - **Monitoring & Lifestyle**:
      - Regular eye pressure checkups and optic nerve monitoring.
      - Avoid skipping medications, as glaucoma damage is permanent.
    - **Next Steps**:
      - Visit an ophthalmologist for pressure test (tonometry) and optic nerve evaluation.
      - Maintain consistent follow-up appointments.
'''

moderate = '''**For Moderate Eye Condition**
- **Recommendation**:
    - **Specialist Consultation**: Moderate stage indicates noticeable disease signs and needs monitoring to prevent worsening.
    - **Possible Treatments**:
      - Medications or supportive therapy depending on the disease category.
      - Lifestyle modification and regular follow-up imaging.
    - **Lifestyle & Monitoring**:
      - Follow-up eye exams every 3–6 months.
      - Manage contributing factors like diabetes, blood pressure, and smoking.
    - **Next Steps**:
      - Consult an ophthalmologist for confirmation and proper management plan.
'''

retina_disease = '''**For Retina Disease**
- **Recommendation**:
    - **Retina Specialist Referral**: Retina diseases can affect vision clarity and may progress if untreated.
    - **Treatment Options (Depends on diagnosis)**:
      - **Medication / Injections**: Anti-VEGF or steroids may be needed.
      - **Laser Treatment**: For retinal tears/leakage.
      - **Surgery**: In severe retinal detachment or advanced retinal damage.
    - **Monitoring & Safety**:
      - If you experience flashes, floaters, or sudden vision loss, seek emergency medical help.
    - **Next Steps**:
      - Get retinal imaging tests (OCT/Fundus exam) from a specialist.
      - Follow specialist recommendations for treatment and follow-ups.
'''

mild = '''**For Mild Eye Condition**
- **Recommendation**:
    - **Early Stage Monitoring**: Mild stage usually indicates early signs of disease and is often manageable with early intervention.
    - **Preventive Measures**:
      - Healthy diet rich in antioxidants and omega-3.
      - Reduce screen strain and maintain good eye hygiene.
      - Control blood sugar and blood pressure if applicable.
    - **Next Steps**:
      - Regular monitoring every 6–12 months.
      - Consult an ophthalmologist for confirmation and guidance.
'''

no_dr = '''**For No Diabetic Retinopathy (No_DR)**
- **Recommendation**:
    - **No DR Detected**: This image shows no signs of diabetic retinopathy.
    - **If you are diabetic**:
      - Maintain strict blood sugar control (HbA1c target as per doctor).
      - Monitor blood pressure and cholesterol regularly.
      - Annual retinal screening is strongly recommended.
    - **Next Steps**:
      - Continue yearly eye exams if diabetic.
      - If not diabetic, routine eye checkups every 1-2 years are sufficient.
'''
armd = '''**For Age-Related Macular Degeneration (ARMD)**
- **Recommendation**:
    - **Specialist Consultation**: ARMD affects the central part of the retina (macula) and can cause central vision loss.
    - **Treatment Options**:
      - **Dry ARMD**: No cure currently, but nutritional supplements (AREDS2 formula) may slow progression.
      - **Wet ARMD**: Anti-VEGF injections (Ranibizumab, Bevacizumab) can help reduce abnormal vessel growth.
      - **Laser Therapy**: In some wet ARMD cases.
    - **Lifestyle & Prevention**:
      - **Diet**: Eat leafy greens, fish, nuts rich in antioxidants and omega-3.
      - **Quit Smoking**: Smoking doubles the risk of ARMD progression.
      - **UV Protection**: Wear sunglasses to reduce UV exposure.
    - **Next Steps**:
      - Consult a retinal specialist immediately.
      - Regular monitoring with OCT scans every 3–6 months.
      - Use an Amsler grid at home to monitor any vision changes.
'''