# imports
import msal

# Replace with your app registration details
client_id = "3714711d-9f73-47e2-9ce8-5f2a01e03049"
tenant_id = "93c1680b-e1a5-4495-a6ba-9d1d4ea523b0"
scopes = ["Group.ReadWrite.All"]  # Adjust scopes as needed
redirect_uri = ("https://login.microsoftonline.com/signin-oidc")  # Where Azure AD redirects after consent

# Create a public client application
app = msal.PublicClientApplication(
    client_id, authority=f"https://login.microsoftonline.com/{tenant_id}"
)

# Get the authorization request URL
auth_url = app.get_authorization_request_url(scopes, redirect_uri=redirect_uri)

# Redirect the user to the authorization URL
print("Please sign in and consent to the requested permissions:")
print(auth_url)

# Get the authorization code from the redirect response
auth_code = input("Enter the authorization code: ")

# Acquire a token using the authorization code
result = app.acquire_token_by_authorization_code(
    auth_code, scopes=scopes, redirect_uri=redirect_uri
)

# Set access token
access_token = result["access_token"]
