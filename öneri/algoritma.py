
from django.shortcuts import render
from .models import User,Resume,Advert
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def recommended_jobs(request, userid):
    try:
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    try:
        cv = Resume.objects.get(userid=userid)
    except Resume.DoesNotExist:
        return JsonResponse({'error': 'CV not found'}, status=404)

    cv_text = cv.category + " " + cv.description
    ilanlar = Advert.objects.all()

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([cv_text] + [ilan.category + " " + ilan.description for ilan in ilanlar])

    benzerlik_skorlari = linear_kernel(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    benzer_ilanlar = sorted(list(enumerate(benzerlik_skorlari)), key=lambda x: x[1], reverse=True)[1:]

    kullanici_onerilen_ilanlar = [{'id': ilan.id, 'title': ilan.title, 'description': ilan.description} for ilan in [ilanlar[i[0]] for i in benzer_ilanlar]]

    response_data = {
        'user': {
            'id': userid,
        },
        'recommended_jobs': kullanici_onerilen_ilanlar,
    }

    return JsonResponse(response_data, status=200)


def get_relevant_applications(request, userid):
    try:
        # Kullanıcının CV verisini veritabanından çekin
        user_cv_data = Resume.objects.filter(userid=userid).first()
        user_cv = user_cv_data.category + " " + user_cv_data.description

        # Tüm CV verilerini veritabanından çekin
        all_cv_data = Resume.objects.values('id', 'category', 'description')

        # Veritabanından çekilen verileri uygun formatta bir listeye dönüştürün
        cv_data = [{'id': data['id'], 'category': data['category'], 'description': data['description']} for data in all_cv_data]

        # Verilen algoritmayı kullanarak benzerlik hesaplaması yapın
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([data['category'] + " " + data['description'] for data in cv_data])
        user_tfidf = tfidf_vectorizer.transform([user_cv])
        cosine_similarities_users = linear_kernel(user_tfidf, tfidf_matrix).flatten()
        similar_users_indices = cosine_similarities_users.argsort()[::-1]
        similar_users_ids = [cv_data[index]['id'] for index in similar_users_indices]
        
        similar_users_applications = Application.objects.filter(userid__in=similar_users_ids)
        user_applications = Application.objects.filter(userid=userid).values_list('advertid', flat=True)
        past_application_ids = similar_users_applications.values_list('advertid', flat=True)
        different_application_ids = list(set(Application.objects.exclude(advertid__in=past_application_ids, userid=userid).values_list('advertid', flat=True)))

        relevant_applications = []
        for index in similar_users_indices:
            similar_user_id = cv_data[index]['id']
            user_applications = Application.objects.filter(userid=similar_user_id).values_list('advertid', flat=True)
            for advertid in user_applications:
                ilan_info = Advert.objects.filter(id=advertid).values('id', 'title', 'category')[0]
                ilan_info["BENZERLIK_ORANI"] = cosine_similarities_users[index]
                relevant_applications.append(ilan_info)

        for advertid in past_application_ids:
            ilan_info = Advert.objects.filter(id=advertid).values('id', 'title', 'category')[0]
            ilan_info["BENZERLIK_ORANI"] = 1
            relevant_applications.append(ilan_info)

        relevant_applications.sort(key=lambda x: x["BENZERLIK_ORANI"], reverse=True)

        # Sonuçları JSON olarak döndürmek üzere hazırlayın
        results = []
        printed_ilan_ids = set()
        for ilan_info in relevant_applications:
            advertid = ilan_info['id']
            if advertid not in printed_ilan_ids:
                ilan_ad = ilan_info['title']
                ilan_alan = ilan_info['category']
                benzerlik_orani = ilan_info['BENZERLIK_ORANI']
                result_dict = {
                    "İLAN İD": advertid,
                    "İLAN ADI": ilan_ad,
                    "İLAN ALAN": ilan_alan,
                    "BENZERLIK_ORANI": benzerlik_orani,
                }
                results.append(result_dict)
                printed_ilan_ids.add(advertid)

        return JsonResponse({"results": results})

    except Exception as e:
        return JsonResponse({"error": str(e)})



#son hali

def get_relevant_applications(request, userid):
    try:
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    try:
        cv = Resume.objects.get(userid=userid)
    except Resume.DoesNotExist:
        return JsonResponse({'error': 'CV not found'}, status=404)

    cv_text = cv.category + " " + cv.description
    ilanlar = Advert.objects.all()

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([cv_text] + [ilan.category + " " + ilan.description for ilan in ilanlar])

    benzerlik_skorlari = linear_kernel(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    benzer_ilanlar = sorted(list(enumerate(benzerlik_skorlari)), key=lambda x: x[1], reverse=True)[1:]

    kullanici_onerilen_ilanlar = [{'id': ilan.id, 'title': ilan.title, 'description': ilan.description} for ilan in [ilanlar[i[0]] for i in benzer_ilanlar]]

    user_cv_data = Resume.objects.filter(userid=userid).first()
    user_cv = user_cv_data.category + " " + user_cv_data.description

    all_cv_data = Resume.objects.values('id', 'category', 'description')
    cv_data = [{'id': data['id'], 'category': data['category'], 'description': data['description']} for data in all_cv_data]

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([data['category'] + " " + data['description'] for data in cv_data])
    user_tfidf = tfidf_vectorizer.transform([user_cv])
    cosine_similarities_users = linear_kernel(user_tfidf, tfidf_matrix).flatten()
    similar_users_indices = cosine_similarities_users.argsort()[::-1]
    similar_users_ids = [cv_data[index]['id'] for index in similar_users_indices]

    similar_users_applications = Application.objects.filter(userid__in=similar_users_ids)
    user_applications = Application.objects.filter(userid=userid).values_list('advertid', flat=True)
    past_application_ids = similar_users_applications.values_list('advertid', flat=True)
    different_application_ids = list(set(Application.objects.exclude(advertid__in=past_application_ids, userid=userid).values_list('advertid', flat=True)))

    relevant_applications = []
    for index in similar_users_indices:
        similar_user_id = cv_data[index]['id']
        user_applications = Application.objects.filter(userid=similar_user_id).values_list('advertid', flat=True)
        for advertid in user_applications:
            ilan_info = Advert.objects.filter(id=advertid).values('id', 'title', 'category')[0]
            ilan_info["BENZERLIK_ORANI"] = cosine_similarities_users[index]
            relevant_applications.append(ilan_info)

    for advertid in past_application_ids:
        ilan_info = Advert.objects.filter(id=advertid).values('id', 'title', 'category')[0]
        ilan_info["BENZERLIK_ORANI"] = 1
        relevant_applications.append(ilan_info)

    relevant_applications.sort(key=lambda x: x["BENZERLIK_ORANI"], reverse=True)

    # Sonuçları JSON olarak döndürmek üzere hazırlayın
    results = []
    printed_ilan_ids = set()
    for ilan_info in relevant_applications:
        advertid = ilan_info['id']
        if advertid not in printed_ilan_ids:
            ilan_ad = ilan_info['title']
            ilan_alan = ilan_info['category']
            benzerlik_orani = ilan_info['BENZERLIK_ORANI']
            result_dict = {
                "İLAN İD": advertid,
                "İLAN ADI": ilan_ad,
                "İLAN ALAN": ilan_alan,
                "BENZERLIK_ORANI": benzerlik_orani,
            }
            results.append(result_dict)
            printed_ilan_ids.add(advertid)

    response_data = {
        'user': {
            'id': userid,
        },
        'recommended_jobs': kullanici_onerilen_ilanlar,
        'relevant_jobs': results
    }

    return JsonResponse(response_data, status=200)
