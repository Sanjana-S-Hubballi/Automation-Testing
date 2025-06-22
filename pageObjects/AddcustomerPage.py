import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//p[normalize-space()='Customers']"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']/p[normalize-space()='Customers']"
    btnAddnew_xpath = "//a[@class='btn btn-primary' and contains(., 'Add new')]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//span[@role='combobox']"
    lstitemAdministrators_xpath =  "//li[contains(., 'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(.,'Registered')]"
    lstitemGuests_xpath = "//li[contains(.,'Guests')]"
    lstitemVendors_xpath = "//li[contains(.,'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender-Male"
    rdFeMaleGender_id = "Gender-Female"
    txtFirstName_xpath = "//input[@id='FirstName' and @name='FirstName']"
    txtLastName_xpath = "//input[@id='LastName' and @name='LastName]"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(1)

        try:
            self.driver.find_element(By.XPATH, "//span[@title='Registered']//span[@class='select2-selection__choice__remove']").click()
        except:
            pass

        role_xpath_map = {
            'Administrators': self.lstitemAdministrators_xpath,
            'Guests': self.lstitemGuests_xpath,
            'Registered': self.lstitemRegistered_xpath,
            'Vendors': self.lstitemVendors_xpath
        }

        self.listitem = self.driver.find_element(By.XPATH, role_xpath_map.get(role, self.lstitemGuests_xpath))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
