def student_info(*arg,**kwargs):
    print(arg)
    print(kwargs)
student_info('math','art',name='lucky',age=21)

        #(or)
courses=['math','art']
info={name='lucky',age=21}
student_info(*courses,**info)
