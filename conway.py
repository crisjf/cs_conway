from brix.test_tools import Conway
table_name = 'conway'
U = Conway(table_name,alive_type='Alive',sleep_time=2)
U.user_sim(quietly=False)