from flask import Flask
FAI=Flask(__name__)
@FAI.route('/stringresponse')
def stringresponse():
    return 'hai this is my first flask project'
@FAI.route('/secondstringresponse')
def secondstringresponse():
    return 'hai this is my second flask project'

if __name__=='__main__':
    FAI.run(debug=True)