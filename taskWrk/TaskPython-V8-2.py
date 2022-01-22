# *** OOP

# Инкапсуляция. Инкапсуляции в Python.


from urllib import request


request = None

class WeatherProvider:
    
    def _request(self):
        url = 'https://weather.by'
        data = request(url, params = {'loc' : 'Minsk'})
        return data
    
    def get_weather(self):
        '''Retrieves weather and return it'''
        data = self._request()
        weather = {'temp' : data['temp']}             

        return weather
    
    def set_location(self):
        '''Setting location of desired place'''
        pass
    
#WeatherProvider()._request()
WeatherProvider().set_location()
# End