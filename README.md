Automatic testing of a "Sinsay" fashion site.
==============================================================================================================================

The structure of the project implemented in Python using unittest is as follows:
--------------------------------
* Module 1: test_open_site.py - verifies the correctness of opening the site. 
* Module 2: test_accept_cookies.py - checks the functionality of the site on different browsers after accepting cookies. 
* Module 3: test_redirect_to_shopping_page.py - verifies the functioning of the site after redirecting to the shopping page in Romania. 
* Module 4: test_search_functionality.py - verifies the correctness of the product search system. 
* Module 5: test_invalid_search.py - checks the behavior of the search system in case of entering an invalid value. 
* Module 6: test_filter_buttons.py - verifies the correct functioning of the filtering buttons. 
* Module 7: test_interactions.py - checks the interaction between the application components and the functionality of the driver.back() button. 
* Module 8: test_return_to_homepage.py - verifies the operation of the return to homepage button by accessing the logo. 
* Module 9: test_add_to_cart.py - checks the correctness of the "Add to Cart" button functionality.
* Module 10: test_social_media_buttons.py - verifies the functionality of the social media buttons and redirects to the corresponding sites.
  
The framework used for automated testing is unittest. By running the automated tests in the unittest framework, we obtained results regarding the correctness of the functioning of various components of the website in different situations and interactions.


The results obtained validated the proper functioning of the site in different tested scenarios, and unittest provided us with the opportunity to automate this process, thereby reducing errors and the time required for manual verification of each aspect.


Test report:
--------------------------------

![Test1](https://github.com/AndreiMihaiC/Unittest/assets/120325527/fda7aabc-3830-4705-a001-773a65c029d6)
![Test12](https://github.com/AndreiMihaiC/Unittest/assets/120325527/2783bcac-dab5-4f0e-98c1-d4e7f7288d0c)

The tests passed successfully, instead the test_add_product_cart test failed with the error message "ElementClickInterceptedExceptionoccurred". This exception occurs when we cannot click on an element due to the existence of another element that blocks access to it.


