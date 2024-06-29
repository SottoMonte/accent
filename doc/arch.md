# Arch

- Model-view-controller (MVC)
- Clean Architecture
- Onion Architecture
- Object–relational mapping
- SDA-WAN o SASE

### Repository/Persistence :
- Collega il Domain Layer ai meccanismi di persistenza dei dati, come i database o i servizi REST.
### Presenter/Controller: 
-Traduce i dati dal Domain Layer in formati comprensibili per la View Layer (ad esempio, per la visualizzazione su un’interfaccia utente).
### Gateway:
- Gestisce l’accesso alle risorse esterne, come API di terze parti o servizi cloud , gestendo l'autenticazione, la memorizzazione nella cache delle risposte , la limitazione della velocità.

## Domain
* Entity (Data) [Repository|Metadata|Event|Exception|Enum|Password|UUID]
* Enum (Data) [Exception|Event]
* Logic (Logic) [Expression|Unique|Union|Be]
* Policy (Data+Logic) [Encrypted]
* Attributed (Data) [Framework|PHP|HTML|Python|Javascript]
## Application
* Use case (Service) [Flow|Run|Load]
* Plug (Manager) [Gateway|Middleware|Controller|Orchestrator|Analyzer|Generator|Optimizer|Builder|Inspector]
* Port (Interface) [Dispatcher|Presentation|Repository|Interaction|Request|Response|Task]
## Border
* Adapter (Interface) [Dispatcher|Presentation|Repository|Interaction|Request|Response|Task]
* Driver (Module/Package/Library) [Framework|Driver|Filesystem|View|Log|Testing|Process|Authentication|Authorization|Encryption|Hashing|Session|SSH|Http|Routing|Translation|Console|CLI|GUI|API]


# Esempi:
## prendere tramite CLI una password e poi salvare la password ricevuta in un file .txt e stampi messaggio di successo
run->application->??->flow->plug(Interaction)->adapter(CLI)->entity(Password)->flow->plug(Presentation)->adapter(Hashing)->flow->plug(Persistence)->adapter(Filesystem)->flow->plug(Dispatcher)->adapter(Redis)->flow->plug(Presentation)->adapter(CLI)

## Analisi Copilot

- Certamente! Analizziamo questo pseudocodice passo per passo:

- run->application: Questo potrebbe rappresentare l’inizio dell’applicazione o del processo.
- ??: Questa parte è ambigua e richiede ulteriori dettagli. Tuttavia, possiamo ipotizzare che sia il punto in cui l’applicazione inizia a interagire con l’utente.
- flow->plug(Interaction)->adapter(CLI): Qui, l’applicazione sembra interagire con l’utente tramite la riga di comando (CLI). L’utente dovrebbe inserire una password.
- entity(Password): L’entità “Password” rappresenta la password inserita dall’utente.
- flow->plug(Presentation)->adapter(Hashing): La password dovrebbe essere elaborata tramite una funzione di hash per proteggerla. L’adapter “Hashing” esegue questa operazione.
- flow->plug(Persistence)->adapter(Filesystem): La password hash dovrebbe essere salvata su un file nel filesystem. L’adapter “Filesystem” gestisce questa operazione.
- flow->plug(Dispatcher)->adapter(Redis): Qui potrebbe esserci un passaggio per inviare la password hash a un sistema di caching come Redis. L’adapter “Redis” gestisce questa operazione.
- flow->plug(Presentation)->adapter(CLI): Infine, l’applicazione dovrebbe restituire un messaggio di successo all’utente tramite la CLI.
- In sintesi, questo pseudocodice rappresenta un flusso di lavoro per ricevere una password dall’utente tramite la riga di comando, elaborarla, salvarla su un file e restituire un messaggio di successo. Tuttavia, alcuni dettagli mancano, come il nome del file in cui viene salvata la password e il contenuto del messaggio di successo.

run->application->start->flow->plug(Interaction)->adapter(CLI)->entity(Password)->flow->plug(Presentation)->adapter(Hashing)->entity(HashedPassword)->flow->plug(Persistence)->adapter(Filesystem)->flow->plug(Presentation)->adapter(CLI)->message(SuccessMessage)