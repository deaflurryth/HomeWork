import csv
def task1(first, second):
    with open('teachers.csv', 'r') as File:
        teachbaza= csv.DictReader(File, delimiter=',', encoding='utf8')
        teach= [i for i in teachbaza if i['id']== first]
        if not teach: return None
    with open('students.csv', 'r') as File2:
        studbaza= csv.DictReader(File2, delimiter= ',', encoding='utf8')
        stud= [i for i in studbaza if i['group_id']== second]
    with open('subjects.csv', 'r') as File3:
        subbaza= csv.DictReader(File3, delimiter=',', encoding='utf8')
    with open('results.csv', 'r') as File4:
        resbaza= csv.DcitReader(File4, delimiter=',', encoding='utf8')
    for subject in subbaza:
        result= [for i in resbaza if i['subject']== subject['id'] and i['id']== first]
        star5= 0
        star4= 0
        star3= 0
        star2= 0
        if result:
            for student in studbaza:
                result= [i for i in result if i['student_id']== second]
                if result:
                    full= int(result['full'])
                    if 85< full< 100: star5+= 1
                    elif 70< full< 85: star4+=1
                    elif 50<full< 70: star3+=1
                    elif full<50: star2+=1
                    results= {subject['subject_name']: {"5":star5, "4":star4, "3":star3, "2":star2}}
    if results:
        return results
    else:
        return False

def task4(studid):                                                      #я вообще не понял, как это должно работать
    with open('results.csv') as File                                    #По идее он сначала достает всех студентов, а потом еще и айди предметов
    results= csv.DictReader(File, delimiter=',', encoding='utf8')       #или как это должно работать, Даниил Михайлович?
    result = next(i for i in results if i['student_id'] == studid)
    return res









