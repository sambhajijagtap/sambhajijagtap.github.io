# sambhajijagtap.github.io
This is a small django application with the following functionality:

A product model with fields: name, description, cost per item, stock quantity, volume.
An admin user can add products using the normal Django admin panel and add the fields name, description, cost, stock quantity. (volume field is not added)
When the product is saved the volume field gets filled automatically. (volume = cost per item * stock quantity)
The admin can see the products as a list and they can only see these fields: name, cost per item, stock quantity and volume. (can not see description field)
Unit tests are added to show that the volume is calculated automatically when the product is saved.
