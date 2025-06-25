package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    "time"
)

type User struct {
    ID               string `json:"id"`
    Name             string `json:"name"`
    Email            string `json:"email"`
    Phone            string `json:"phone"`
    RegistrationTime string `json:"registrationTime"`
}

func main() {
    http.HandleFunc("/ping", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprint(w, "user-info-service: pong")
    })
    http.HandleFunc("/users/", func(w http.ResponseWriter, r *http.Request) {
        id := r.URL.Path[len("/users/"):]
        user := User{
            ID:               id,
            Name:             fmt.Sprintf("User %s", id),
            Email:            fmt.Sprintf("user%s@example.com", id),
            Phone:            "+1234567890",
            RegistrationTime: time.Now().Format(time.RFC3339),
        }
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(user)
    })
    log.Println("User Info Service running on port 8081")
    log.Fatal(http.ListenAndServe(":8081", nil))
}