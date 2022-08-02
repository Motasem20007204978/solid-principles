
# Solid Responsibility Principle 

# the class should only have one reason to change.
# eg. the class is about Student registration,
#    should not be also about Student learning process.

# do one thing, do it well.

# should be just one reason to go to the class to make changes
# eg. goto Student class to chagne the way to register a student
#   not the way to register courses to a student or send emails.

# specilize the class name to do one thing, do it well.


from abc import abstractclassmethod


class StudentRegistration:

    @staticmethod
    def register(**informaion):
        # gather information about the student and register them
        # to check the information validity, make it in other functions
        if Validation.validate_information(**informaion):
            # save the information to the database
            StudentRegistration.save_data(**informaion)
            # send the report to the student
            report = Report.create_report(**informaion)
            Email.send_email(informaion['email'], report)
            print(f"Registering {informaion['name']}")
    
    @staticmethod
    def save_data(**informaion):
        # save the information to the database
        print(f"Saving data for {informaion['name']}")


class StudentModification:

        @staticmethod
        def modify(identity, **informaion):
            # to check the information validity
            if Validation.validate_information(**informaion):
                # resave the information to the database
                StudentModification.edit_data(identity, **informaion)
                # send the report to the student
                report = Report.create_report(**informaion)
                Email.send_email(informaion['email'], report)
                print(f"Modifying {informaion['name']}")
        
        @staticmethod
        def edit_data(identity, **informaion):
            # edit the information to the database
            print(f"Saving data for {identity}")


class StudentDeletion:
        
        @staticmethod
        def delete(identity):
            # check the student information from the database
            information = GetStudent.get_student(identity)

            if information:
                # delete the student from the database
                StudentDeletion.delete_data(identity)
                # send the report to the student
                report = Report.create_report(**information)
                Email.send_email(information['email'], report)
                print(f"Deleting {identity}")
        
        @staticmethod
        def delete_data(identity):
            # delete the student from the database
            print(f"Deleting {identity}")


class GetStudent:

        @staticmethod
        def get(identity):
            # get the student from the database
            information = GetStudent.get_data(identity)
            if information:
                return information

        @staticmethod    
        def get_data(identity):
            # get the student from the database
            print(f"Getting {identity}")
            return identity

class Email:

    @staticmethod
    def send_email(email, report):
        # sending process
        print(f"Sending email to {email}")


class Report:

    @staticmethod
    def create_report(**informaion):
        # creating process
        report = f"{informaion['name']} has been registered"
        return report


class Validation:

    @staticmethod
    def validate_information(**informaion) -> bool:
        # check the information validity
        # if it is valid, register the student
        # if it is not valid, send an email to the student
        valid_name = __class__.validate_nama(informaion["name"])
        valid_id = __class__.validate_identity( informaion["identity"])
        valid_email = __class__.validate_email(informaion["email"])
        valid_address = __class__.validate_address(informaion["address"])
        valid_phone = __class__.validate_phone_number(informaion["phone_number"])
        
        print(f"Validating information for {informaion['name']}")

        return all([valid_name, valid_id, valid_email, valid_address, valid_phone])

    @staticmethod
    def validate_email(email) -> bool:
        # validate the email process
        print(f"Validating email for {email}")
        return True
    
    @staticmethod
    def validate_address(address) -> bool:
        # validate the address process
        print(f"Validating address for {address}")
        return True
        
    @staticmethod
    def validate_phone_number(phone_number) -> bool:
        # validate the phone number process
        print(f"Validating phone number for {phone_number}")
        return True

    @staticmethod
    def validate_identity(identity) -> bool:
        # validate the identity process
        print(f"Validating identity for {identity}")
        return True

    @staticmethod
    def validate_nama(name) -> bool:
        # validate the name process
        print(f"Validating name for {name}")
        return True


class Course:
    
    @staticmethod
    @abstractclassmethod
    def python_course():
        # create a course
        ...

    @staticmethod
    @abstractclassmethod
    def java_course():
        # create a course
        ...



    