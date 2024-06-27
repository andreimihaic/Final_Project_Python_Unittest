<h1>Automation Project for SINSAY</h1>

The purpose of this project is to use all acquired Python automated testing knowledge and apply it, such as: to ensure correct and optimal functionality, user authentication, product search, purchase process and overall site performance- of the web.

Application under test: SINSAY

Tools used: Unittest

Project description: The main purpose of this site's automated testing is to check functionality consistently and efficiently by running a series of predefined tests on different aspects of the site, such as navigation, forms, links and overall user experience.

<ol>
<h2> The structure of the project implemented in Python using unittest is as follows: </h2>
<br>

<ul>
  <li> Module 1: TestWebsiteOpen - verifies the correctness of opening the site. </li>
  
``` 
It initializes a Chrome WebDriver (self.driver) and opens the Sinsay website (https://www.sinsay.com/).
The window is maximized, and an implicit wait of 5 seconds is set. 
It checks whether the title of the opened website matches the expected title.
If the titles don’t match, an assertion error with a custom message is raised. 
```
  <li> Module 2: TestAcceptCookies - checks the functionality of the site on different browsers after accepting cookies. </li>

``` 
ACCEPT_COOKIES: This stores a tuple representing the selector for the “accept cookies” button on the Sinsay websiteIt

setUp(self) method: Initializes an empty list self.drivers to store WebDriver instances.

create_driver(self, browser) method:  Creates a WebDriver instance for the specified browser (Chrome, Firefox, or Edge).
                                      Opens the Sinsay website.
                                      Maximizes the window and sets an implicit wait of 5 seconds for each instance.

test_accept_cookies(self) method:   For each browser in the browsers list, a WebDriver instance is created.
                                    It finds the cookies banner element and clicks the accept button.
                                    Verifies whether the cookies banner is correctly displayed after acceptance.

If the cookies banner is not displayed correctly after acceptance, the test will report an error
```
  <li> Module 3: TestGoTOStore - Verify if, after accepting cookies, the ‘Go to store’ button on the Sinsay website leads the user to the expected URL. </li>

```
test_go_to_store method:  First, it clicks the cookie acceptance button.
                          Then, it waits for the “Go to store” button to be visible and clickable.
                          It compares the actual URL with the expected URL and displays an error if they don’t match.
```  
  <li> Module 4: TestHeaderIsDisplayed - verifies the correctness of the product search system. </li>

```
test_header_is_displayed Method:  First, it clicks the cookie acceptance button.
                                  Then, it waits for the “Go to store” button to be clickable .
                                  Finally, it checks whether the header element is displayed.
```

  <li> Module 5: TestCheckSearchButtonIsDisplayed - checking whether the search button on the Sinsay website is displayed correctly. </li>
  
```
test_search_button_is_displayed method:   This method checks if the search button is displayed on the page.
                                          It clicks the “Accept Cookies” button and then the “Go to store” button.
                                          It finds the search button and verifies if it is displayed.
                                          If it is not displayed, an error will be raised with the message “The search button is not visible.
```  
  <li> Module 6: TestSearchProducts - checking whether the search button and product results on the Sinsay website function correctly. </li>
  
```
test_search_products method:  Clicks the “Accept Cookies” button and then the “Go to store” button.
                              Clicks the search button.
                              Enters the text “telefon” into the search field and presses the “Enter” key.
                              Waits for products to be displayed on the page.
                              Collects the text of the products and prints them to the console.
                              Verifies that at least one product result is displayed.
```  
  <li> Module 7: TestFilterProducts - checks the interaction between the application components and the functionality of the driver.back() button. </li>

```
test_filter_products method:  Clicks the “Accept Cookies” button and then the “Go to store” button.
                              Clicks the search button.
                              Enters the text “tricouri” (T-shirts) into the search field and presses the “Enter” key.
                              Accesses product characteristics (categories, gender, size, and colors).
                              Selects the category, gender (male), size (L), and color (white).
                              Verifies if the displayed products contain the text “Tricou” (T-shirt).
```  
  <li> Module 8: TestNotFoundProduct - verify the behavior when a product is not found on the website. </li>

```
test_not_found_product method:  Accepts cookies.
                                Clicks the “Go to store” button .
                                Clicks the search button.
                                Enters the text “inexistent” into the search field and presses the Enter key.
                                Checks if the error message “Nu s-au putut găsi produsele pentru fraza introdusă” appears. If it doesn’t, the test fails.
```  
  <li> Module 9: TestSortListAscending - check the filtering functionality of the product.</li>

```
test_filter_products method:   Clicks the cookie acceptance button.
                                Clicks the search button.
                                Finds the search input field and enters the text “caiet”
                                Presses the Enter key.
                                Collects all product elements from the list.
                                Sorts the product list by price.
                                Displays product names and prices in the console.
                                Verifies that products are sorted in ascending order by price.
```    
  <li> Module 10: TestNavigateBack - check that the back navigation in the browser works correctly on the site.</li>

```
search_for_product method:  Click the search button.
                            Locate the search input element and enter the text “pantofi”
                            Press the Enter key.

click_fifth_product method:   Collect all product elements from the list.
                              Choose the fifth product from the list and click on it.

test_navigate_back method:  Search for the product “pantofi”
                            Select the fifth product.
                            While the current URL is different from the initial URL, navigate back.
                            Verify if the initial URL is the same as the current URL.
```    
  <li> Module 11: TestReturnHomepage - checks whether the correct return to the homepage occurs after performing specific actions on the website.</li>

```
locators : The keys represent the names of elements we will search for on the page, and the values are tuples containing two elements: the locator type and the locator value .

test_return_homepage method:  It clicks the cookie acceptance button, then the search button.
                              It enters the text “tricouri” into the search input field.
                              It finds and clicks the brand logo.
                              It checks if the current URL matches the initial URL. If it does, the test passes; otherwise, it fails.
                              An additional check ensures that the URL contains “www.sinsay.com.”
```  
  <li> Module 12: TestAuthenticationWithEmptyFields - check the login behavior on the site, when the data entry fields are empty. </li>

```
test_authentication_with_empty_fields method:   It clicks the cookie acceptance button and then the link to the store.
                                                It finds and clicks the account button (represented by an account icon).
                                                It defines an input_data list with two empty elements (for email and password).
                                                It finds the email input field and enters empty text.
                                                It finds the password input field and enters empty text.
                                                It clicks the authentication button.
                                                It checks if the “This field is required” error message appears.
```    
  <li> Module 13: TestAuthenticationWrongUserAndPassword - check the website login behavior when an incorrect username and password are provided.</li>

```
test_wrong_username_and_password method:  Accepts cookies.
                                          Clicks the “Go to store” button.
                                          Clicks the account icon.
                                          Enters incorrect authentication data (email address and password) into the corresponding fields.
                                          Presses the login button.
                                          Verifies if the displayed error message ends with the text “nevalidă.”
```   
  <li> Module 14: TestSocialMediaIcons - check if the social network icons are displayed correctly on the web page.</li>

```
test_share_buttons method:  Accepts cookies.
                            Clicks the “Go to store” button.
                            Identifies all social media icons within a specific container.
                            Verifies if each icon is displayed on the page.
```    
  <li> Module 15: TestChangeLanguage - check the functionality of changing the language on a website.</li>

```
test_change_language method:  Waits for the “Accept Cookies” button to be clickable and then clicks it.
                              Finds the language selector and clicks on it.
                              Locates the language option and clicks it.
                              Selects the desired language (“Global store”).
                              Clicks the “Go to store” button.
                              Uses “soft” assertions to verify that the current URL contains ‘en’ (indicating the English version of the website).
``` 
  
</ul><br>

<ol>
<h2> Test report </h2>
<br>  
  
The framework used for automated testing is unittest. By running the automated tests in the unittest framework, we obtained results regarding the correctness of the functioning of various components of the website in different situations and interactions.


The results obtained validated the proper functioning of the site in different tested scenarios, and unittest provided us with the opportunity to automate this process, thereby reducing errors and the time required for manual verification of each aspect.

![Test Results 1](https://github.com/andreimihaic/MySQL_Project-Car-seles/assets/120325527/afd5991a-907b-4987-baf3-b5a664bbf57f)
![Test Results 2](https://github.com/andreimihaic/MySQL_Project-Car-seles/assets/120325527/6fb97579-7fa5-48a6-bb34-54231a770b3d)

</ol>
<h2> Conclusions </h2>

  While no major product risks were identified, we recommend prioritizing the implementation of critical functionality for the product’s success. 
  As part of the launch preparation, consider conducting additional performance testing and ensuring compatibility across various devices. 
  A key lesson learned is the importance of comprehensive testing to address potential issues before launch. Effective communication within the development team is also crucial. These insights should inform future projects for optimal outcomes.


