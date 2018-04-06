import re


class IValidator:
    def do_validation(self, new_empid, new_gender, new_age, new_sales, new_bmi, new_salary, new_birthday):
        raise NotImplementedError("The do_validation abstract method has not been implemented")


class Validator(IValidator):
    def __init__(self):
        self.empid_pattern = "^[A-Z][\d]{3}$"
        self.gender_pattern = "^(M|F)$"
        self.age_pattern = "^[\d]{2}$"
        self.sales_pattern = "^[\d]{3}$"
        self.BMI_pattern = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary_pattern = "^([\d]{2}|[\d]{3})$"
        self.birthday = "^(0[1-9]|[1-2][0-9]|3(0|1))(-|/)(0[1-9]|1[0-2])(-|/)(19|20)[0-9]{2}$"

    def do_validation(self, new_empid, new_gender, new_age, new_sales, new_bmi, new_salary, new_birthday):
        issue = ''
        result = True
        if not self.__validate_part(self.empid_pattern, new_empid):
            result = False
            raise Exception('empid is not valid')

        if not self.__validate_part(self.gender_pattern, new_gender):
            result = False
            raise Exception('gender is not valid')

        if not self.__validate_part(self.age_pattern, new_age):
            result = False
            raise Exception('age is not valid')

        if not self.__validate_part(self.sales_pattern, new_sales):
            result = False
            raise Exception('sales is not valid')

        if not self.__validate_part(self.BMI_pattern, new_bmi):
            result = False
            raise Exception('BMI is not valid')

        if not self.__validate_part(self.salary_pattern, new_salary):
            result = False
            raise Exception('Salary is not valid')

        if not self.__validate_part(self.birthday, new_birthday):
            result = False
            raise Exception('Birthday is not valid')
        return result

    @staticmethod
    def __validate_part(self, rule, value):
        matching = re.match(rule, value)
        if matching is None:
            return False
        else:
            return True

if __name__ =="_main__":
    test_validator = IValidator()
    if test_validator.do_validation('A123', 'Fafafda', '24', '123', 'Normal', '20', '12-08-1990'):
        print("yes")
    else:
        print("no")