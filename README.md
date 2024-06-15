<h1>Automation Project for SINSAY</h1>

The purpose of this project is to use all acquired Python automated testing knowledge and apply it, such as: to ensure correct and optimal functionality, user authentication, product search, purchase process and overall site performance- of the web.

Application under test: SINSAY

Tools used: Unittest

Project description: The main purpose of this site's automated testing is to check functionality consistently and efficiently by running a series of predefined tests on different aspects of the site, such as navigation, forms, links and overall user experience.

<ol>
<li> The structure of the project implemented in Python using unittest is as follows: </li>
<br>

<ul>
  <li> Module 1: test_open_site.py - verifies the correctness of opening the site. </li>
  <li> Module 2: test_accept_cookies.py - checks the functionality of the site on different browsers after accepting cookies. </li>
  <li> Module 3: test_redirect_to_shopping_page.py - verifies the functioning of the site after redirecting to the shopping page in Romania. </li>
  <li> Module 4: test_search_functionality.py - verifies the correctness of the product search system. </li>
  <li> Module 5: test_invalid_search.py - checks the behavior of the search system in case of entering an invalid value. </li>
  <li> Module 6: test_filter_buttons.py - verifies the correct functioning of the filtering buttons. </li>
  <li> Module 7: test_interactions.py - checks the interaction between the application components and the functionality of the driver.back() button. </li>
  <li> Module 8: test_return_to_homepage.py - verifies the operation of the return to homepage button by accessing the logo. </li>
  <li> Module 9: test_add_to_cart.py - checks the correctness of the "Add to Cart" button functionality.</li>
  <li> Module 10: test_social_media_buttons.py - verifies the functionality of the social media buttons and redirects to the corresponding sites.</li>
</ul><br>

<ol>
<h2> Test report </h2>
<br>  
  
The framework used for automated testing is unittest. By running the automated tests in the unittest framework, we obtained results regarding the correctness of the functioning of various components of the website in different situations and interactions.


The results obtained validated the proper functioning of the site in different tested scenarios, and unittest provided us with the opportunity to automate this process, thereby reducing errors and the time required for manual verification of each aspect.

![Test1](https://github.com/AndreiMihaiC/Unittest/assets/120325527/fda7aabc-3830-4705-a001-773a65c029d6)
![Test12](https://github.com/AndreiMihaiC/Unittest/assets/120325527/2783bcac-dab5-4f0e-98c1-d4e7f7288d0c)

</ol>
<h2> Conclusions </h2>

The tests passed successfully, instead the test_add_product_cart test failed with the error message "ElementClickInterceptedExceptionoccurred". This exception occurs when we cannot click on an element due to the existence of another element that blocks access to it.


