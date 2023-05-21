import Cookies from "universal-cookie";

export default async function AuthRoute() {
    let is_authenticated = false;
  
    const cookies = new Cookies();
    const token = cookies.get("token");
  
    const body = { token: token };
  
    const response = await fetch("http://localhost:8000/api/get-decoded-token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body)
    });
    const response_json = await response.json();
    is_authenticated = response_json["auth"];
  
    return is_authenticated;
  }