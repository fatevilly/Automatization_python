from lesson7.Data_types.Pages.Mainpage import MainPage
from lesson7.Data_types.Pages.Datafieldes import DataFild

def test_assertion(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.find_fields()
    main_page.filling_in_the_fields()
    main_page.click_submit_button()

    data_field = DataFild(chrome_browser)
    data_field.find_fields()
    data_field.get_class_first_name()
    data_field.get_class_last_name()
    data_field.get_class_address()
    data_field.get_class_email()
    data_field.get_class_phone()
    data_field.get_class_city()
    data_field.get_class_jobposition()
    data_field.get_class_company()
    data_field.get_class_zipcode()

    assert "success" in data_field.get_class_first_name()
    assert "success" in data_field.get_class_last_name()
    assert "success" in data_field.get_class_address()
    assert "success" in data_field.get_class_email()
    assert "success" in data_field.get_class_phone()
    assert "success" in data_field.get_class_city()
    assert "success" in data_field.get_class_country()
    assert "success" in data_field.get_class_jobposition()
    assert "success" in data_field.get_class_company()
    assert "danger" in data_field.get_class_zipcode()