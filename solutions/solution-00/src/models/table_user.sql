CREATE TABLE User (
    id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert initial data (optional)
INSERT INTO User (id, username, email, password_hash, is_admin, created_at, updated_at)
VALUES ('1', 'admin', 'admin@example.com', 'hashed_password', TRUE, NOW(), NOW());
