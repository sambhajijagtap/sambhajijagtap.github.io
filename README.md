This is a small django application with the following functionality:

1. A product model with fields: name, description, cost per item, stock quantity, volume.
2. An admin user can add products using the normal Django admin panel and add the fields name, description, cost, stock quantity. (volume field is not added)
3. When the product is saved the volume field gets filled automatically. (volume = cost per item * stock quantity)
4. The admin can see the products as a list and they can only see these fields: name, cost per item, stock quantity and volume. (can not see description field)
5. Unit tests are added to show that the volume is calculated automatically when the product is saved.
