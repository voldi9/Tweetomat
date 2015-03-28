TWEETOMAT v1.0

Program jest prosty w obsłudze: wyznacza on oceny słowom kluczowym ('#') i użytkownikom ('@') wymienianym w tweetach na podstawie ilosci retweet'ów i favorites'ów tych tweetów oraz tego jak dawno zostały one opublikowane. W zarządzaniu można dodać/usunąć obserwowanych użytkowników, jak również aktywować/dezaktywować ich obserwację (ta operacja nie usuwa ich tweetów z bazy). Odświeżanie bazy może nie działać przy zbyt częstych próbach z powodu ograniczeń API twittera.

Do obsługi programu potrzebne są biblioteki pythona psycopg2 i twython, które zawarte są w folderze lib. Odpalając ./install.sh w tym folderze dodajemy biblioteki do swoich ścieżek pythona. Następnie w folderze tweetomat program odpala się poleceniem python main.py.
