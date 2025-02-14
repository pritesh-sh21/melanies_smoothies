# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("🥤 Customize Your Smoothie! 🥤")
st.write(
   
   """
   """
)


session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))
# st.dataframe(data=my_dataframe, use_container_width=True)


name_on_order=st.text_input("Name on Smoothie:")
st.write('The name on your Smoothie will be: ',name_on_order)

ingrediants_list=st.multiselect('Choose up to 5 ingrediants:',my_dataframe,max_selections=5)



if ingrediants_list:

    ingredients_string=''
    
    for x in ingrediants_list:
        ingredients_string+=x+' '
    # st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order+  """')"""

    sub_button=st.button('Submit Order')
    st.write(my_insert_stmt)
    if sub_button:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")


    
