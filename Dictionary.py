student_data = {'id1': 
 {'name': ['Sara'],
  'class': ['V'],
   'subjects': ['Math, English,Science']                       }
},
student_data = {'id2': 
 {'name': ['David'],
  'class': ['V'],
   'subjects': ['Math, English,Science']                       }
},
student_data = {'id3': 
 {'name': ['Sara'],
  'class': ['V'],
   'subjects': ['Math, English,Science']                       }
},
student_data = {'id4': 
 {'name': ['Surya'],
  'class': ['V'],
   'subjects': ['Math, English,Science']                       
   },
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)