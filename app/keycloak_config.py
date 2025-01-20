from keycloak import KeycloakOpenID
import os

keycloak_openid = KeycloakOpenID(
    server_url=os.getenv("http://localhost:8080/") + "/realms/master",
    client_id="file-manager",
    realm_name="master",
    client_secret_key="c93S4ANKU7rTuDhjL9u0eqP61CyvQdGV"
)
