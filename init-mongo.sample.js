db.createUser(
    {
        user: "user",
        pwd: "your-password",
        roles : [
            {
                role: "readWrite",
                db: "your-db"
            }
        ]
    }
)
