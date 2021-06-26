CREATE TABLE 'user_info' (
    'id' int 11 NOT NULL AUTO_INCREMENT PRIMARY KEY,
    'email' varchar(100) NOT NULL,
    'password' varchar(100) NOT NULL,
    'firstname' varchar(100) NOT NULL,
    'lastname' varchar(100) NOT NULL,
    'phonenumber' varchar(100) NOT NULL
    )
    ENGINE=InnoDB DEFAULT CHARSET=latin1