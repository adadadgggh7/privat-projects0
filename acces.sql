
CREATE TABLE Films (
    MovieID AUTOINCREMENT PRIMARY KEY,
    Title TEXT(100) NOT NULL,
    Genre TEXT(50),
    Duration INTEGER,
    Rating TEXT(10),
    Director TEXT(100),
    Description MEMO,
    ReleaseDate DATE
);


CREATE TABLE Halls (
    HallID AUTOINCREMENT PRIMARY KEY,
    HallName TEXT(50) NOT NULL,
    Capacity INTEGER,
    Type TEXT(20)
);


CREATE TABLE Screenings (
    ScreeningID AUTOINCREMENT PRIMARY KEY,
    MovieID LONG NOT NULL,
    HallID LONG NOT NULL,
    StartTime DATETIME NOT NULL,
    EndTime DATETIME NOT NULL,
    Price CURRENCY,
    CONSTRAINT FK_Movie FOREIGN KEY (MovieID) REFERENCES Films(MovieID),
    CONSTRAINT FK_Hall FOREIGN KEY (HallID) REFERENCES Halls(HallID)
);


CREATE TABLE Seats (
    SeatID AUTOINCREMENT PRIMARY KEY,
    HallID LONG NOT NULL,
    RowNumber INTEGER NOT NULL,
    SeatNumber INTEGER NOT NULL,
    Type TEXT(20),
    CONSTRAINT FK_SeatHall FOREIGN KEY (HallID) REFERENCES Halls(HallID)
);


CREATE TABLE Customers (
    CustomerID AUTOINCREMENT PRIMARY KEY,
    FirstName TEXT(50) NOT NULL,
    LastName TEXT(50) NOT NULL,
    Phone TEXT(20),
    Email TEXT(100),
    RegistrationDate DATETIME DEFAULT NOW()
);


CREATE TABLE Bookings (
    BookingID AUTOINCREMENT PRIMARY KEY,
    CustomerID LONG NOT NULL,
    ScreeningID LONG NOT NULL,
    BookingDate DATETIME DEFAULT NOW(),
    TotalAmount CURRENCY,
    PaymentStatus TEXT(20),
    CONSTRAINT FK_Customer FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CONSTRAINT FK_Screening FOREIGN KEY (ScreeningID) REFERENCES Screenings(ScreeningID)
);


CREATE TABLE Tickets (
    TicketID AUTOINCREMENT PRIMARY KEY,
    BookingID LONG NOT NULL,
    SeatID LONG NOT NULL,
    Price CURRENCY,
    TicketStatus TEXT(20),
    CONSTRAINT FK_Booking FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID),
    CONSTRAINT FK_Seat FOREIGN KEY (SeatID) REFERENCES Seats(SeatID)
);
