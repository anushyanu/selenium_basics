# commanda:
     application commands
        get() - opening the application url
        title - capture the tittle of the current webpage
        current_url - capture the current url of the web page
        page_source -  capture the source code of the page
    conditional commands
        is_displayed()
        is_enabled()
        is_selected()
    # browser commands
        close()
        quit()
    # navigational ommands
        back()
        forward()
        refresh()

    # wait commands
    implicitily wait
    explicitily wait


text vs get_attribute("id/class/value")
text - captures the inner text
get_attribute is present inside the tag such as id="",class="",value=""

whenever you want to enter the keyboard ---> use submit()


* implicit wait is used in the beginning and it applies for all according to the time used.
    if still page doesnot load within time then it throws an error.

* time.sleep is worse becoz even the page loaded the default behaviour is to wait until time
if gets if over:

* explicit wait works based on condition.explicit wait  has declaration and utilisations.
declaration as two parameters.one is driver and two is seconds.
mywait = WebDriverWait(driver,10) # this is declarations.webdriverwait is the class.

**** MOUSE OPERATIONS ******
act = ActionChains(driver) # is a class used for mouse operations
mouse_hover -> move_to_element(element).perform()
right_click -> context_click(element).perform()
double_click -> double_click(element).perform()
drag_and_drop -> drag_and_drop(source,target).perform()
slider -> drag_and_drop_by_offset(source,x,y) # before this to find the position use .location it is not method.




