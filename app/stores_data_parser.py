import json

class StoresDataParser:
  def __init__(self, f, required_fields = ("name","postcode")):
    self.required_fields = required_fields
    self.__data = []
    with open(f) as file:
      file_content = json.load(file)
      for row in file_content:
        self.__data.append(self.__validate_row(row, required_fields ))
      
  def __validate_row(self, row, required_fields):
      valid_dict = {}
      for field in required_fields:
        if field in row:
          valid_dict[field] = row[field]
        else:
          print("TO DO: add error handling")
      return valid_dict

  def get_data(self):
    return self.__data

