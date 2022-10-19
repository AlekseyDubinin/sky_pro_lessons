
CREATE TABLE IF NOT EXISTS suppliers (
    id smallint PRIMARY KEY,
    company_name character varying(40) NOT NULL,
    contact_name character varying(30),
    contact_title character varying(30),
    country character varying(15),
    city character varying(15),
    postal_code character varying(10),
    region character varying(15),
    address character varying(60),
    phone character varying(100),
    fax character varying(100),
    homepage character varying(100)
);


INSERT INTO suppliers VALUES (1, 'Exotic Liquids', 'Charlotte Cooper', ' Purchasing Manager', 'UK', ' ', ' EC1 4SD', ' London', ' 49 Gilbert St.', '(171) 555-2222', '', '');
INSERT INTO suppliers VALUES (2, 'New Orleans Cajun Delights', 'Shelley Burke', ' Order Administrator', 'USA', ' LA', ' 70117', ' New Orleans', ' P.O. Box 78934', '(100) 555-4822', '', '#CAJUN.HTM#');
INSERT INTO suppliers VALUES (3, 'Grandma Kelly Homestead', 'Regina Murphy', ' Sales Representative', 'USA', ' MI', ' 48104', ' Ann Arbor', ' 707 Oxford Rd.', '(313) 555-5735', '(313) 555-3349', '');
INSERT INTO suppliers VALUES (4, 'Tokyo Traders', 'Yoshi Nagase', ' Marketing Manager', 'Japan', ' ', ' 100', ' Tokyo', ' 9-8 Sekimai Musashino-shi', '(03) 3555-5011', '', '');
INSERT INTO suppliers VALUES (5, 'Cooperativa de Quesos Las Cabras', 'Antonio del Valle Saavedra', ' Export Administrator', 'Spain', ' Asturias', ' 33007', ' Oviedo', ' Calle del Rosal 4', '(98) 598 76 54', '', '');
INSERT INTO suppliers VALUES (6, 'Mayumis', 'Mayumi Ohno', ' Marketing Representative', 'Japan', ' ', ' 545', ' Osaka', ' 92 Setsuko Chuo-ku', '(06) 431-7877', '', 'Mayumi s (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/mayumi.htm#');
INSERT INTO suppliers VALUES (7, 'Pavlova, Ltd.', 'Ian Devling', ' Marketing Manager', 'Australia', ' Victoria', ' 3058', ' Melbourne', ' 74 Rose St. Moonie Ponds', '(03) 444-2343', '(03) 444-6588', '');
INSERT INTO suppliers VALUES (8, 'Specialty Biscuits, Ltd.', 'Peter Wilson', ' Sales Representative', 'UK', ' ', ' M14 GSD', ' Manchester', ' 29 King s Way', '(161) 555-4448', '', '');
INSERT INTO suppliers VALUES (9, 'PB Knäckebröd AB', 'Lars Peterson', ' Sales Agent', 'Sweden', ' ', ' S-345 67', ' Göteborg', ' Kaloadagatan 13', '031-987 65 43', '031-987 65 91', '');
INSERT INTO suppliers VALUES (10, 'Refrescos Americanas LTDA', 'Carlos Diaz', ' Marketing Manager', 'Brazil', ' ', ' 5442', ' Sao Paulo', ' Av. das Americanas 12.890', '(11) 555 4640', '', '');
INSERT INTO suppliers VALUES (11, 'Heli Süßwaren GmbH & Co. KG', 'Petra Winkler', ' Sales Manager', 'Germany', ' ', ' 10785', ' Berlin', ' Tiergartenstraße 5', '(010) 9984510', '', '');
INSERT INTO suppliers VALUES (12, 'Plutzer Lebensmittelgroßmärkte AG', 'Martin Bein', ' International Marketing Mgr.', 'Germany', ' ', ' 60439', ' Frankfurt', ' Bogenallee 51', '(069) 992755', '', 'Plutzer (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/plutzer.htm#');
INSERT INTO suppliers VALUES (13, 'Nord-Ost-Fisch Handelsgesellschaft mbH', 'Sven Petersen', ' Coordinator Foreign Markets', 'Germany', ' ', ' 27478', ' Cuxhaven', ' Frahmredder 112a', '(04721) 8713', '(04721) 8714', '');
INSERT INTO suppliers VALUES (14, 'Formaggi Fortini s.r.l.', 'Elio Rossi', ' Sales Representative', 'Italy', ' ', ' 48100', ' Ravenna', ' Viale Dante, 75', '(0544) 60323', '(0544) 60603', '#FORMAGGI.HTM#');
INSERT INTO suppliers VALUES (15, 'Norske Meierier', 'Beate Vileid', ' Marketing Manager', 'Norway', ' ', ' 1320', ' Sandvika', ' Hatlevegen 5', '(0)2-953010', '', '');
INSERT INTO suppliers VALUES (16, 'Bigfoot Breweries', 'Cheryl Saylor', ' Regional Account Rep.', 'USA', ' OR', ' 97101', ' Bend', ' 3400 - 8th Avenue Suite 210', '(503) 555-9931', '', '');
INSERT INTO suppliers VALUES (17, 'Svensk Sjöföda AB', 'Michael Björn', ' Sales Representative', 'Sweden', ' ', ' S-123 45', ' Stockholm', ' Brovallavägen 231', '08-123 45 67', '', '');
INSERT INTO suppliers VALUES (18, 'Aux joyeux ecclésiastiques', 'Guylène Nodier', ' Sales Manager', 'France', ' ', ' 75004', ' Paris', ' 203, Rue des Francs-Bourgeois', '(1) 03.83.00.68', '(1) 03.83.00.62', '');
INSERT INTO suppliers VALUES (19, 'New England Seafood Cannery', 'Robb Merchant', ' Wholesale Account Agent', 'USA', ' MA', ' 02134', ' Boston', ' Order Processing Dept. 2100 Paul Revere Blvd.', '(617) 555-3267', '(617) 555-3389', '');
INSERT INTO suppliers VALUES (20, 'Leka Trading', 'Chandra Leka', ' Owner', 'Singapore', ' ', ' 0512', ' Singapore', ' 471 Serangoon Loop, Suite #402', '555-8787', '', '');
INSERT INTO suppliers VALUES (21, 'Lyngbysild', 'Niels Petersen', ' Sales Manager', 'Denmark', ' ', ' 2800', ' Lyngby', ' Lyngbysild Fiskebakken 10', '43844108', '43844115', '');
INSERT INTO suppliers VALUES (22, 'Zaanse Snoepfabriek', 'Dirk Luchte', ' Accounting Manager', 'Netherlands', ' ', ' 9999 ZZ', ' Zaandam', ' Verkoop Rijnweg 22', '(12345) 1212', '(12345) 1210', '');
INSERT INTO suppliers VALUES (23, 'Karkki Oy', 'Anne Heikkonen', ' Product Manager', 'Finland', ' ', ' 53120', ' Lappeenranta', ' Valtakatu 12', '(953) 10956', '', '');
INSERT INTO suppliers VALUES (24, 'G day, Mate', 'Wendy Mackenzie', ' Sales Representative', 'Australia', ' NSW', ' 2042', ' Sydney', ' 170 Prince Edward Parade Hunter s Hill', '(02) 555-5914', '(02) 555-4873', 'G day Mate (on the World Wide Web)#http://www.microsoft.com/accessdev/sampleapps/gdaymate.htm#');
INSERT INTO suppliers VALUES (25, 'Ma Maison', 'Jean-Guy Lauzon', ' Marketing Manager', 'Canada', ' Québec', ' H1J 1C3', ' Montréal', ' 2960 Rue St. Laurent', '(514) 555-9022', '', '');
INSERT INTO suppliers VALUES (26, 'Pasta Buttini s.r.l.', 'Giovanni Giudici', ' Order Administrator', 'Italy', ' ', ' 84100', ' Salerno', ' Via dei Gelsomini, 153', '(089) 6547665', '(089) 6547667', '');
INSERT INTO suppliers VALUES (27, 'Escargots Nouveaux', 'Marie Delamare', ' Sales Manager', 'France', ' ', ' 71300', ' Montceau', ' 22, rue H. Voiron', '85.57.00.07', '', '');
INSERT INTO suppliers VALUES (28, 'Gai pâturage', 'Eliane Noz', ' Sales Representative', 'France', ' ', ' 74000', ' Annecy', ' Bat. B 3, rue des Alpes', '38.76.98.06', '38.76.98.58', '');
INSERT INTO suppliers VALUES (29, 'Forêts d érables', 'Chantal Goulet', ' Accounting Manager', 'Canada', ' Québec', ' J2S 7S8', ' Ste-Hyacinthe', ' 148 rue Chasseur', '(514) 555-2955', '(514) 555-2921', '');
