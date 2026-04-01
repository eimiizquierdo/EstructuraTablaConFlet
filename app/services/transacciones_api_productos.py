#app/services/transacciones_api_productos.py
import httpx
from app.components.error import ApiError

BASE = "http://localhost:8000/products"
TIME_OUT = 10.0

# Obtiene la lista de productos de FastAPI
async def list_products(limit: int = 20, offset: int = 0) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{BASE}/", params={"limit": limit, "offset": offset}, timeout=TIME_OUT)
            if 200 <= r.status_code < 300:
                return r.json() if r.content else {}
            raise ApiError(f"Error {r.status_code}: {r.text}", r.status_code)
    except httpx.TimeoutException:
        raise ApiError("El servidor tardó demasiado en responder", 0)
    except httpx.ConnectError:
        raise ApiError("No se pudo conectar al servidor", 0)
    except httpx.RequestError as e:
        raise ApiError(f"Error de conexión: {str(e)}", 0)

# Obtiene el producto con el id que se le pasa como parámetro
async def get_product(product_id: str) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{BASE}/{product_id}", timeout=TIME_OUT)
            if 200 <= r.status_code < 300:
                return r.json() if r.content else {}
            raise ApiError(f"Error {r.status_code}: {r.text}", r.status_code)
    except httpx.TimeoutException:
        raise ApiError("El servidor tardó demasiado en responder", 0)
    except httpx.ConnectError:
        raise ApiError("No se pudo conectar al servidor", 0)
    except httpx.RequestError as e:
        raise ApiError(f"Error de conexión: {str(e)}", 0)

# Crea un producto nuevo
async def create_product(data: dict) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{BASE}/", json=data, timeout=TIME_OUT)
            if 200 <= r.status_code < 300:
                return r.json() if r.content else {}
            raise ApiError(f"Error {r.status_code}: {r.text}", r.status_code)
    except httpx.TimeoutException:
        raise ApiError("El servidor tardó demasiado en responder", 0)
    except httpx.ConnectError:
        raise ApiError("No se pudo conectar al servidor", 0)
    except httpx.RequestError as e:
        raise ApiError(f"Error de conexión: {str(e)}", 0)

# Actualiza el producto
async def update_product(product_id: str, data: dict) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            r = await client.put(f"{BASE}/{product_id}", json=data, timeout=TIME_OUT)
            if 200 <= r.status_code < 300:
                return r.json() if r.content else {}
            raise ApiError(f"Error {r.status_code}: {r.text}", r.status_code)
    except httpx.TimeoutException:
        raise ApiError("El servidor tardó demasiado en responder", 0)
    except httpx.ConnectError:
        raise ApiError("No se pudo conectar al servidor", 0)
    except httpx.RequestError as e:
        raise ApiError(f"Error de conexión: {str(e)}", 0)

# Elimina el producto
async def delete_product(product_id: str) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            r = await client.delete(f"{BASE}/{product_id}", timeout=TIME_OUT)
            if 200 <= r.status_code < 300:
                return r.json() if r.content else {}
            raise ApiError(f"Error {r.status_code}: {r.text}", r.status_code)
    except httpx.TimeoutException:
        raise ApiError("El servidor tardó demasiado en responder", 0)
    except httpx.ConnectError:
        raise ApiError("No se pudo conectar al servidor", 0)
    except httpx.RequestError as e:
        raise ApiError(f"Error de conexión: {str(e)}", 0)

# Para probar (ejecutar con: python -m app.services.transacciones_api_productos)
if __name__ == "__main__":
    import asyncio
    
    async def test():
        try:
            productos = await list_products(limit=5, offset=0)
            print("Productos:", productos)
        except ApiError as e:
            print(f"Error: {e}")
    
    asyncio.run(test())