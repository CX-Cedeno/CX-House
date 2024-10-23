using System;
using System.Data.SqlClient;
using System.IO;

class VulnerableApp
{
    // 1. Inyección SQL
    public static void SqlInjectionExample(string username)
    {
        string connectionString = "your_connection_string";
        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            connection.Open();
            string query = $"SELECT * FROM Users WHERE Username = '{username}'"; // Vulnerable a inyección SQL
            SqlCommand command = new SqlCommand(query, connection);
            SqlDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                Console.WriteLine(reader["Username"]);
            }
        }
    }

    // 2. Exposición de datos sensibles
    public static void ReadSensitiveFile()
    {
        string filePath = Console.ReadLine(); // Lectura de archivos sin validación
        using (StreamReader reader = new StreamReader(filePath))
        {
            Console.Wr
