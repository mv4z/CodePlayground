/*
Martin Vazquez
CSC 355 Section 501 
Assignment 2 
January 22, 2020 */

DROP TABLE BOOKING;
DROP TABLE TRAVELER;
DROP TABLE TOUR;

CREATE TABLE TRAVELER(
	TrID NUMBER(5) PRIMARY KEY,
	TrName VARCHAR2(20),
	TrPhone NUMBER(10)
	);

CREATE TABLE TOUR(
	TID VARCHAR2(4) PRIMARY KEY,
	DestinationName VARCHAR2(85),
	TLength NUMBER(3,0) 
			CHECK(0 < TLength ),

	TCost NUMBER(6,2)
			CHECK(0 <= TCost AND TCost <= 9999.99)
	);

CREATE TABLE BOOKING(
	TourID VARCHAR2(4),
	TravelerID NUMBER(5),
	TourDate DATE,

	PRIMARY KEY(TourID, TravelerID),

	FOREIGN KEY(TourID)
		REFERENCES TOUR(TID),
	FOREIGN KEY (TravelerID)
		REFERENCES TRAVELER(TrID)
	);

insert into tour values (4232, 'London', 14, 659.00);
insert into tour values (4300, 'Rome', 7, 982.00);
insert into tour values (4400, 'Seattle', 5, 325.00);
insert into tour values (4500, 'NYC', 14, 515.00);

insert into TRAVELER values(44444, 'Martin Vazquez Jr.', 6302958270);
insert into TRAVELER values(44445, 'Dimitri Vazquez', 7732028927);
insert into TRAVELER values(44446, 'Romeo Vazquez', 8477322388);

insert into BOOKING values(4300, 44445, date '2020-02-01' );
insert into BOOKING values(4500, 44446, date '2020-02-04' );
insert into BOOKING values(4500, 44444, date '2020-02-04' );
insert into BOOKING values(4232, 44444, date '2020-03-24' );
insert into BOOKING values(4400, 44445, date '2020-07-01' );

select * from TRAVELER;
select * from TOUR;
select * from BOOKING;