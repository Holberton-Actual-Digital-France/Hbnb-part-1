-- Create User table
CREATE TABLE User (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create State table
CREATE TABLE State (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create City table
CREATE TABLE City (
    id VARCHAR(36) PRIMARY KEY,
    state_id VARCHAR(36) NOT NULL,
    name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (state_id) REFERENCES State(id)
);

-- Create Place table
CREATE TABLE Place (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    city_id VARCHAR(36) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    number_rooms INTEGER DEFAULT 0,
    number_bathrooms INTEGER DEFAULT 0,
    max_guest INTEGER DEFAULT 0,
    price_by_night INTEGER DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (city_id) REFERENCES City(id)
);

-- Create Review table
CREATE TABLE Review (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    place_id VARCHAR(36) NOT NULL,
    text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (place_id) REFERENCES Place(id)
);

-- Create Amenity table
CREATE TABLE Amenity (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create PlaceAmenity table
CREATE TABLE PlaceAmenity (
    place_id VARCHAR(36) NOT NULL,
    amenity_id VARCHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES Place(id),
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id)
);

-- Insert initial data (examples)
INSERT INTO User (id, email, password, is_admin) VALUES
('1', 'user@example.com', 'securepassword', FALSE);

INSERT INTO State (id, name) VALUES
('1', 'California');

INSERT INTO City (id, state_id, name) VALUES
('1', '1', 'San Francisco');

INSERT INTO Amenity (id, name) VALUES
('1', 'WiFi');

INSERT INTO Place (id, user_id, city_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude) VALUES
('1', '1', '1', 'Lovely Place', 'A lovely place in San Francisco', 2, 1, 4, 100, 37.7749, -122.4194);

INSERT INTO Review (id, user_id, place_id, text) VALUES
('1', '1', '1', 'Great place to stay!');

INSERT INTO PlaceAmenity (place_id, amenity_id) VALUES
('1', '1');
